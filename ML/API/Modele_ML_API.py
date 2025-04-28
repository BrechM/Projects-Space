import statsmodels.api as sm
import shap
import numpy as np
from sklearn.linear_model import LinearRegression
from fastapi import FastAPI
from pydantic import BaseModel

np.random.seed(0)

# Génération des données
taille_pere_init = np.random.uniform(160, 190, 100)
taille_mere_init = np.random.uniform(150, 180, 100)
bruit = np.random.normal(0, 5, 100)

taille_enfant_init = 0.5 * taille_pere_init + 0.4 * taille_mere_init + 30 * bruit

data_global = {
    "taille_pere": taille_pere_init.tolist(),
    "taille_mere": taille_mere_init.tolist(),
    "taille_enfant": taille_enfant_init.tolist() 
}

# Création du modèle statsmodels (non utilisé pour shap)
x_sm = sm.add_constant(np.column_stack((taille_pere_init, taille_mere_init)))
modele_sm = sm.OLS(taille_enfant_init, x_sm).fit()

# Création du modèle sklearn pour SHAP
modele_sklearn = LinearRegression()
modele_sklearn.fit(np.column_stack((taille_pere_init, taille_mere_init)), taille_enfant_init)

# SHAP Explainer
explainer = shap.Explainer(modele_sklearn, np.column_stack((taille_pere_init, taille_mere_init)))
shap_values = explainer(np.column_stack((taille_pere_init, taille_mere_init)))

# Visualisation SHAP
X = np.column_stack((taille_pere_init, taille_mere_init))
shap.summary_plot(shap_values, features=X, feature_names=["taille_pere", "taille_mere"])

# Création de l'API FastAPI
app = FastAPI()

class EntreePrediction(BaseModel):
    taille_pere: float
    taille_mere: float

class NouvellesDonnees(BaseModel):
    taille_pere: list[float]
    taille_mere: list[float]
    taille_enfant: list[float]

@app.get("/")
def accueil():
    return {'message': "Bienvenue sur notre API de prédiction de la taille d'un enfant"}

@app.post("/predire/")
def predire(donnees: EntreePrediction):
    x = np.array([donnees.taille_pere, donnees.taille_mere]).reshape(1, -1)
    prediction = modele_sklearn.predict(x)[0]  # [0] pour obtenir la première prédiction
    explainer = shap.Explainer(modele_sklearn, np.column_stack((taille_pere_init, taille_mere_init)))
    shap_values = explainer(x)
    
    return {
        "prediction": prediction,
        "valeurs_shap": shap_values.values[0].tolist()  # Liste des valeurs SHAP pour cette prédiction
    }

@app.get("/parametres/")
def obtenir_parametres():
    noms_variables = ["Intercept", "taille_pere", "taille_mere"]
    coeffs = modele_sklearn.coef_.tolist()
    coeffs.insert(0, modele_sklearn.intercept_)

    r2 = modele_sm.rsquared  
    p_valeurs = modele_sm.pvalues.tolist()
    significativite = ["Significatif" if p < 0.05 else "Non significatif" for p in modele_sm.pvalues]

    return {
        "noms_variables": noms_variables,
        "coefficients": coeffs,
        "r2": r2,
        "p_valeurs": p_valeurs,
        "significativite": significativite
    }

@app.post("/ajouter_donnees/")
def ajouter_donnees(data: NouvellesDonnees):
    global modele_sklearn, modele_sm, data_global

    # Mise à jour des données
    data_global["taille_pere"].extend(data.taille_pere)
    data_global["taille_mere"].extend(data.taille_mere)
    data_global["taille_enfant"].extend(data.taille_enfant)

    X = np.column_stack((data_global["taille_pere"],  data_global["taille_mere"]))
    y = np.array(data_global["taille_enfant"])

    # Réentraînement du modèle sklearn
    modele_sklearn = LinearRegression().fit(X, y)

    # Réentraînement du modèle statsmodels
    X_sm = sm.add_constant(X)
    modele_sm = sm.OLS(y, X_sm).fit()

    # Nouveaux paramètres du modèle
    noms_variables = ["Intercept", "taille_pere", "taille_mere"]
    coeffs = modele_sklearn.coef_.tolist()
    coeffs.insert(0, modele_sklearn.intercept_)

    r2 = modele_sm.rsquared
    p_valeurs = modele_sm.pvalues.tolist()
    significativite = ["Significatif" if p < 0.05 else "Non significatif" for p in modele_sm.pvalues]

    return {
        "message": "Données ajoutées et modèle mis à jour",
        "nouveaux_parametres": {
            "noms_variables": noms_variables,
            "coefficients": coeffs,
            "r2": r2,
            "p_valeurs": p_valeurs,
            "significativite": significativite
        }
    }

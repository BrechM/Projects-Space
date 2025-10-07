# Etape 2 : Inference avec le Modele Random Forest
# Organisation du répertoire de travail
# - TutoDockerML/
# - data/
#       - wine_data.csv
#       - batch_input.csv
# - models/
#       - random_forest.pkl
# - scripts/
#       - train_model
#       - inference.py

# %% Importation des bibliotheques
import pandas as pd
import numpy as np
import joblib
import os

# %% Chargement du modele
model_path = "C:/Users/User/Desktop/workspace/Projects-Space/ML/Projet6/models/random_forest_model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Le ficher {model_path} n'existe pas. Assurer-vous d'avoir entrainé et sauvegardé votre modele.")

model = joblib.load(model_path)
print("Modele chargé avec succès.")

# %% Inference - Single Prediction
def single_prediction(input_features):
    """"
    Realise une prediction unique avec le modele

    Arguments :
    - inputs_features  list ou np.array des caracteristiques (doit correspondre à l'ordre du modele)

    Retour :
    - Classe prédite
    """
    input_array = np.array(input_features).reshape(1, -1) # convertit les features en tableau numpy
    # reshape(1, -1) → redimensionne le tableau : [5.1, 3.5, 1.4, 0.2] devient [[5.1, 3.5, 1.4, 0.2]]
    # on a maintenant un tableau 1 ligne et 5 colonnes
    # -1 colonnes → numpy devine automatiquement le nombre de colonnes.
    # Sans ça, le modèle croirait qu’on lui donne une seule feature au lieu d’un vecteur complet.

    prediction = model.predict(input_array)[0] # En ajoutant [0], tu prends le premier (et unique) élément du tableau
    
    # Cela renvoie un tableau numpy (ex : [0] ou [1]).
    # [0] → on prend uniquement la première valeur (car on ne prédit qu’un seul individu).
    return prediction

# %% Exemple de prediction unique
sample_input = [13.0, 2.0, 2.3, 15.0, 100.0, 2.8, 3.0, 0.3, 1.7, 6.0, 1.0, 3.0, 1000.0]
# Chaque element de cette liste represente chaque var explicative, en excluant target
predicted_class = single_prediction(sample_input)
print(f"Prédiction pour l'ensemble donné : Classe {predicted_class}")
# la sortie sera une prediction de target

# La classe predite est la classe 0

# %% Inference - Batch Prediction
def batch_prediction(input_file, output_file):
    """
    Réalise une prédiction par lot en utilisant un fichier CSV comme entrée.

    Arguments :
    - input_file : str, chemin du fichier CSV contenant les données d'entrée
    - output_file : str, chemin où sauvegarder les résultats

    Retour :
    - Aucun (les résultats sont sauvegardés dans output_file)
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Le fichier d'entrée {input_file} n'existe pas")
    
    # Chargement des données 
    input_data = pd.read_csv(input_file)
    print("Données d'entrée chargées avec succes")

    # Predictions
    predictions = model.predict(input_data)

    # Ajout des prédictions aux données
    input_data["prediction"] = predictions

    # Sauvegarde des résultats
    input_data.to_csv(output_file, index=False) # Avec index=False, on dit à pandas de ne pas enregistrer l’index 
    # → seules les colonnes réelles sont sauvegardées.
    print(f"Les résultats ont été sauvegardé dans {output_file}.")

# %% Exemple de prediction par lot
batch_input_path = "C:/Users/User/Desktop/workspace/Projects-Space/ML/Projet6/data/batch_input.csv" # chemin vers un fichier csv avec des caractéristiques
batch_output_path = "C:/Users/User/Desktop/workspace/Projects-Space/ML/Projet6/data/batch_predictions.csv" # chemin pour sauvegarder les resultats

# Création d'un exemple de fichier batch_input.csv pour demonstration
exemple_batch_data = pd.DataFrame([
    [13.0, 2.0, 2.3, 15.0, 100.0, 2.8, 3.0, 0.3, 1.7, 6.0, 1.0, 3.0, 1000.0],
    [12.5, 1.5, 2.1, 14.0, 90.0, 2.6, 2.9, 0.25, 1.6, 5.8, 1.1, 2.8, 950.0]
], columns=[
    "alcohol", "malic_acid", "ash", "alcalinity_of_ash", "magnesium", "total_phenols", "flavanoids", 
    "nonflavanoid_phenols", "proanthocyanins", "color_intensity", "hue", "od280/od315_of_diluted_wines", "proline"
])

exemple_batch_data.to_csv(batch_input_path, index=False)

# %% Execution de la prediction par lot
batch_prediction(batch_input_path, batch_output_path)

# %%

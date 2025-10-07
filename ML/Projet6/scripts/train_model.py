# Etape 1: Entrainemnet du modele ML

# Organisation du repertoire de travail
# - Projet6/
#   - data/
#        - wine_data.csv
#   - models/
#        - logistic_regression_model.pkl
#   - scripts/
#       - train_model.py        

#%% Importation des bibliotheques 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import joblib
import os


#%% Création des repertoires pour l'organisation
print(os.getcwd()) # Identification du chemin d'acces
os.makedirs("C:/Users/User/Desktop/workspace/Projects-Space/ML/Projet6/data", exist_ok=True)
os.makedirs("C:/Users/User/Desktop/workspace/Projects-Space/ML/Projet6/models", exist_ok=True) 

#%% Chargement et préparation des données
# Chargement des données wine de sklearn
data = load_wine()
print(data)
x = pd.DataFrame(data.data, columns=data.feature_names)
y= pd.Series(data.target,name="target")
print(x)
print(y)
#%% Ajout de la cible aux données pour une sauvegarde
data_df = pd.concat([x, y], axis=1) # axis=1, concatenation par colonnes
data_df.to_csv("C:/Users/User/Desktop/workspace/Projects-Space/ML/Projet6/data/wine_data.csv", index=False)
print("Les données ont été sauvegardées dans data/wine_data.csv")

# %% Exploration rapide des données
print("Apercu des premieres lignes :")
print(data_df.head())
print("\nDescription statistique")
print(data_df.describe())

# Detail de la variable cible, qui a trois modalités
data_df.target.value_counts()

# %% Visualisation de la distribution des variables 
for column in x.columns[:5]: # limitation à 5 colonnes pour cet exemple
    plt.figure(figsize=(6, 4))
    x[column].hist(bins=20, color="skyblue", edgecolor="black")
    plt.title(f"distribution de {column}")
    plt.xlabel(column)
    plt.ylabel("Frequence")
    plt.show()
# %% division des données en ensemble d'entrainement
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# %% Entrainement du modele
model=RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)
print("Modele entrainé avec succes.")

# %% Evaluation du modele
# Predictions
y_pred = model.predict(x_test)

# Rapport de classification
print("\nRapport de clssification :") # \n caractère qui signifie "saut de ligne"
print(classification_report(y_test, y_pred))

# Matrice de confusion
cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm, display_labels=data.target_names).plot(cmap="Blues")
plt.title("Matrice de confusion")
plt.show()

# %% Sauvegarde du modele
model_path = "C:/Users/User/Desktop/workspace/Projects-Space/ML/Projet6/models/random_forest_model.pkl"
joblib.dump(model, model_path)
print(f"Le modele a été sauvegardé dans {model_path}.")
# %%

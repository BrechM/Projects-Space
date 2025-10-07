# Etape 3 : Streamlit App pour consommer le Modele Random Forest
# Organisation du répertoire :
# - TutoDockerML/
#   - app/
#       -app.py (ce fichier)
#   - data/
#       - batch_input.csv
#       - batch_predictions.csv
#   - models/
#       - random_forest_model.pkl
#   - Dockerfile

# %% Importation des bibliotheques

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Determiner le chemin absolu du modele
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Donc BASE_DIR = le dossier où se trouve ce script Python.
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "random_forest_model.pkl") # ".." : permet de remonter d'un dossier 

# -------------------------------------------------------
# os.path.abspath(__file__) renvoie "C:/Users/User/Desktop/workspace/Projects-Space/ML/projet6/app.py"
# os.path.dirname(...) renvoie le dossier parent du chemin fourni, ici:
# "C:/Users/User/Desktop/workspace/Projects-Space/ML/projet6
# On stocke ce chemin de dossier dans une variable BASE_DIR. Ça permet de définir une racine de projet 
# pour facilement construire des chemins relatifs.
# --------------------------------------------------------


# Charger le modele
if not os.path.exists(MODEL_PATH):
    st.error(f"Le fichier {MODEL_PATH} n'existe pas. Assurez-vous d'avoir entrainé et sauvegardé le modèle")
    st.stop()

model = joblib.load(MODEL_PATH)

# Fonctions pour les prédictions

# définition d'une fonction pour valider la caractéristique des vars d'entrée

expected_columns = [
        "alcohol", "malic_acid", "ash", "alcalinity_of_ash", "magnesium", "total_phenols", "flavanoids", 
        "nonflavanoid_phenols", "proanthocyanins", "color_intensity", "hue", "od280/od315_of_diluted_wines", "proline"
    ]

def validate_single_input(input_data):
    """"Valide les caractéristiques d'entrée pour une prédiction unique"""
    if not isinstance(input_data, dict):
        return False, "Les données doivent etre un dictionnaire."

    for col in expected_columns:
        if col not in input_data:
            return False, f"Caractéristique manquante : {col}"
        if not isinstance(input_data[col], (int, float)):
            return False, f"La caractéristique '{col}' doit etre un nombre."
    
    return True, ""

def single_prediction(input_features):
    input_array = np.array([input_features[col] for col in input_features]).reshape(1, -1)
    prediction = model.predict(input_array)[0] # En ajoutant [0], tu prends le premier (et unique) élément du tableau
    return prediction

def batch_prediction(input_file):
    input_data = pd.read_csv(input_file)

    # Validation des colonnes
    """Cette ligne vérifie que input_data contient touts les colonnes attendues"""
    if not all(col in input_data.columns for col in expected_columns):
        return None, f"Le fichier doit contenir les colonnes suivantes : {', '.join(expected_columns)}" # ',' pour separer les differentes colonnes
    
    # Predictions
    predictions = model.predict(input_data[expected_columns])
    input_data["prediction"] = predictions

    # Creer le repertoire ../data s'il n'existe pas 
    output_dir = os.path.join(BASE_DIR, "..", "data")
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "batch_predictions.csv")
    input_data.to_csv(output_file, index=False)
    return output_file, ""


# ---------------------- Interface Streamlit ----------------------
st.title(" 🔮 Application de Prédiction - Random Forest ")
st.write("Cette application permet de tester le modèle sur une entrée unique ou un fichier CSV.")

# Choix du mode
mode = st.radio("Choisissez un mode :", ["🔹 Prédiction unique", "🔹 Batch Prediction (CSV)"])

if mode == "🔹 Prédiction unique":
    st.subheader("Entrer les caractéristiques")
    input_data = {}
    for col in expected_columns:
        input_data[col] = st.number_input(f"{col}", value=0.0, format="%.4f")

    if st.button("Prédire"):
        valid, msg = validate_single_input(input_data)
        if not valid:
            st.error(msg)
        else:
            prediction = single_prediction(input_data)
            st.success(f"✅ Classe prédite : {prediction}")

elif mode == "🔹 Batch Prediction (CSV)":
    st.subheader("Charger un fichier CSV")
    uploaded_file = st.file_uploader("Sélectionner un fichier CSV", type=["csv"])

    if uploaded_file is not None:
        output_file, msg = batch_prediction(uploaded_file)
        if output_file is None:
            st.error(msg)
        else:
            st.success("✅ Prédictions terminées !")
            st.write("Téléchargez le fichier des prédictions ci-dessous :")
            with open(output_file, "rb") as f:
                st.download_button("📥 Télécharger CSV", f, file_name="batch_predictions.csv", mime="text/csv")
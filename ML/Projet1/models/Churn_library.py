# La modularisation du code va consister à ecrire des fonctions pythons qui vont permettre de 
# generer le process de A à Z

# La modularisation fait ce qui a été fait sur le Notebook mais de facon automatique

"""
This is the churn_libary.py python file that used to find customers who are likely to churn
The execution of this file will produce artefacts in images and models folders.
Date: April 02, 2023
"""
import os
import logging
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import RocCurveDisplay, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import FunctionTransformer, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import joblib  

# Pour la journalisation
logging.basicConfig(
    filename='C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/logs/churn_library.log',
    level= logging.INFO,
    filemode='w',
    format='%(names)s - %(levelname)s - %(message)s')

# Importation des données

def import_data(path):
    """
    returns dataframe for the csv found at path

    input:
        path: a path to the csv
    output:
        df: pandas dataframe
    """
    df = pd.read_csv(path)
    df.drop('customerID', axis=1, inplace=True)
    df['Churn'] = df['Churn'].apply(lambda val: 0 if val == "No" else 1)

    return df 

# Split des données

def data_spliting(df):
    """
    input:
            df: pandas dataframe
    output:
            train: training dataframe
            validate: validation dataframe
            test: test dataframe
    """ 
    train, test = train_test_split(
        df, test_size=0.3, random_state=123, stratify=df['Churn']
    )
    test, validate = train_test_split(
        test, test_size=0.5, random_state=123, stratify=test['Churn']
    )

    # Enregistrement des differents ensembles de données
    train.to_csv('C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/data/train.csv', index=False)
    validate.to_csv('C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/data/validation.csv', index=False)
    test.to_csv('C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/data/test.csv', index=False)

    X_train, X_val = train.drop(
        'Churn', axis=1), validate.drop(
        'Churn', axis=1)
    y_train, y_val = train['Churn'], validate['Churn']

    return train, X_train, y_train, X_val, y_val 

# Exploration visuelle des données

def perform_eda(df):
    """
    perform eda on df and save figures to images folder
    input:
            df: a pandas dataframe
    output:
            None
    """
    df_copy = df.copy()

    list_columns = df_copy.columns.to_list()

    list_columns.append('Heatmap')

    df_corr = df_copy.corr(numeric_only=True)

    for column_name in list_columns:
        plt.figure(figsize=(10, 6))
        if column_name == 'Heatmap':
            sns.heatmap(
                df_corr,
                mask=np.triu(np.ones_like(df_corr, dtype=bool)),
                center=0, cmap='RdBu', linewidths=1, annot=True,
                fmt=".2f", vmin=-1, vmax=1
            )
        else:
            if df[column_name].dtype != 'O':
                df[column_name].hist()
            else:
                sns.countplot(data=df, x=column_name)
        plt.savefig("C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/images/eda/" + column_name + ".jpg")
        plt.close()

# Fonction rapport de classification

def classification_report_image(y_train,
                                y_train_preds,
                                y_val,
                                y_val_preds):
    """
    produces classification report for training and testing results and stores report as image
    in images folder
    input:
            y_train: training response values
            y_train_preds: training predictions from logistic regression
            y_val: validation response values
            y_val_preds: validation predictions from logistic regression
    output:
            None
    """
    class_reports_dico = {
        "Logistic Regression train results": classification_report(
            y_train,
            y_train_preds),
            # classification_report est une fonction sklearn.metrics
        "Logistic Regression validation results": classification_report(
            y_val,
            y_val_preds)}

    for title, report in class_reports_dico.items():
        plt.rc('figure', figsize=(7, 3))
        plt.text(
            0.2, 0.3, str(report), {
                'fontsize': 10}, fontproperties='monospace')
        plt.axis('off')
        plt.title(title, fontweight='bold')
        plt.savefig("C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/images/results/" + title + ".jpg")
        plt.close()

# Fonction pour régler le probleme de la colonne 'TotalCharges'

def convert_totalcharges(X):
    # X : dataframe
    Z = X.copy()
    Z['TotalCharges'] = pd.to_numeric(Z['TotalCharges'], errors='coerce')
    return Z.values # .values me retourne un tableau numpy


def build_pipeline():
    numeric_features = [
        'SeniorCitizen', 
        'tenure', 
        'MonthlyCharges', 
        'TotalCharges'
    ]

    categorical_fetures = [
        'gender',
        'Partner',
        'Dependents',
        'PhoneService',
        'MultipleLines',
        'InternetService',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
        'Contract',
        'PaperlessBilling',
        'PaymentMethod',
    ]

    # Pipeline de prétraitement des variables indépendantes numériques
    numeric_transformer = Pipeline(
        steps=[('convert', FunctionTransformer(convert_totalcharges)),
               ('inputer', SimpleImputer(strategy='median')),
               ('scaler', StandardScaler())]
    )

    # Pipeline de prétraitement des variables indépendantes qualitatives
    categorical_transformer = Pipeline(
        steps=[
            ('OneHotEncoder',
             OneHotEncoder(
                 sparse_output=False,
                 handle_unknown='ignore'))])
    
    # Combinaison des deux précedents pipelines en un seul
    preprocessor = ColumnTransformer(
        transformers=[
            ('numeric',
             numeric_transformer,
             numeric_features),
            ('categorical',
             categorical_transformer,
             categorical_fetures)])
    
    # Pipeline de modélisation
    pipeline_model = Pipeline(
        steps=[('preprocessor', preprocessor),
               ('logreg', LogisticRegression(solver='newton-cg', # On recupere nos reglages d'hyperparametre
                                             random_state=123,
                                             max_iter=2000,
                                             C=5.0,
                                             penalty='12'))]
    )
    return pipeline_model

# Creation d'une fonction train_models
def train_models(X_train, X_val, y_train, y_val):
    """
    train, store model results: images + scores, and store models
    input:
            X_train: X training data
            X_val: X validation data
            y_train: y training data
            y_val: y validation data
    output:
            None
    """
    # Formation du modele
    model = build_pipeline()
    model.fit(X_train, y_train)

    # Predictions
    y_train_preds_lr = model.predict(X_train)
    y_val_preds_lr = model.predict(X_val)

    # ROC curves image
    lrc_plot = RocCurveDisplay.from_estimator(model, X_val, y_val)
    plt.savefig("C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/images/results/roc_curve.jpg")
    plt.close()

    # Classification reports images
    classification_report_image(
        y_train,
        y_train_preds_lr,
        y_val,
        y_val_preds_lr)
    
    # Sauvegarde du modele
    joblib.dump(model, 'C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/models/logreg_model.pkl')

    # Fonction qui va executer toutes les etapes 

    def main():
        logging.info("Importation des données...")
        raw_data = import_data("C:/Users/brech/Desktop/dossier de taff/ML/Projet 1/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
        logging.info("Importation des données : SUCCES")

        logging.info("Division des données...")
        train_data, Xtrain, ytrain, Xval, yval = data_spliting(raw_data)
        logging.info("Division des données : SUCCES")

        logging.info("Analyse exploratoire des données...")
        perform_eda(train_data)
        logging.info("Analyse exploratoire des données : SUCCES")

        logging.info("Formation du modele...")
        train_models(Xtrain, Xval, ytrain, yval)
        logging.info("Formation du modele : SUCCES")

    if __name__ == "__main__":
        print("Execution en cours...")
        main()
        print("Fin de l'Execution avec succes")
# Librairies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
from PyPDF2 import PdfMerger

# On va commencer par creer une fonction qui va nous permettre de generer chaque graphique 

# On commence avec le diagramme à barres
def wine_quality_bar(data):
    sns.countplot(data=data, x="quality")
    plt.xlabel('qualité', fontweight="bold")
    plt.title('Score de qualité du vin', fontweight="bold")
    plt.savefig('wine_quality.Pdf', orientation="landscape")
    plt.close()

# On va recuper le heatmap
def heatmap_cor(data):
    plt.figure(figsize=(12, 12))
    mask = np.triu(np.ones_like(data.corr(), dtype=bool))
    sns.heatmap(data.corr(), mask=mask, center=0, cmap='RdBu', linewidths=1, annot=True, fmt=".2f", vmin=-1, vmax=1)
    plt.title('Coefficient de corrélation de Pearson entre variables', fontweight="bold") # comprendre le parametre fontsize
    plt.savefig('wine_heatmap.pdf', orientation='landscape')
    plt.close()

# Ensuite la boxplot
def save_qualityvsfeats_fig(data):
    feats = data.select_dtypes(include = ['float64']).columns.to_list() # on tient compte que des float
    for col in feats:
        Pearson_coef, P_value = st.pearsonr(data[col], data["quality"])
        aff = 'Coef.Pearson =' + str(round(Pearson_coef, 3)) + ', P-valeur = ' + str(round(P_value, 3))
        sns.boxplot(x=data['quality'], y=data[col])
        plt.xlabel('Score de qualité du vin', fontweight="bold")
        plt.ylabel(col, fontweight="bold")
        plt.title('quality VS ' + col + '.' + aff, fontweight="bold")
        plt.savefig(col + 'VS quality.pdf', orientation='landscape') 
        plt.close()

#  On va maintenant creer une fonction qui va nous generer un rapport

def create_graphics_report(file):
    df = pd.read_csv(file, delimiter=";")
    wine_quality_bar(df) # 1ere fonction que j'ai crée
    heatmap_cor(df) # 2eme fonction
    save_qualityvsfeats_fig(df) # 3eme fonction

    # On peut maintenant merger ces pdf crées(pour automatiser le tout)
    merger = PdfMerger()
    pdf_files = ["wine_quality.Pdf", "wine_heatmap.pdf"] + [
        col + 'VS quality.pdf' 
        for col in df.select_dtypes(include = ['float64']).columns
        ]
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write("Wine_DataViz_Reporting.pdf")
    merger.close()

if __name__ == "__main__":
    file = input("Renseignez le nom de votre fichier de données  CSV :")
    create_graphics_report(file)

# Pour lancer mon script, dans le terminal, on lance "python generate-report.py"
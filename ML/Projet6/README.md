
# Deployement d'un model ML avec Docker et Streamlit

## Introduction

Ce projet illustre le cycle de vie complet du déploiement d’un modèle de machine learning, depuis l’entraînement et les tests d’inférence jusqu’à la création d’une application Dockerisée pour une distribution et une scalabilité optimales.

Docker, une plateforme de conteneurisation, est un pilier de l’ingénierie moderne en machine learning. Elle permet aux développeurs de packager des applications et leurs dépendances dans des conteneurs portables qui s’exécutent de manière cohérente sur différents environnements. Avec Docker, les modèles ML peuvent être déployés facilement, en garantissant reproductibilité et compatibilité, que ce soit sur la machine locale du développeur ou dans le cloud

---

## Etape du projet

Ce projet comportera les etapes clés suivantes:

### 1. Entrainement et sauvegarde du model

- Entrainement d'un model ML en utilisant une base de données
- Sauvegarde du modele entrainé dans un format qui pourrait etre facilement déployé (e.g .pkl ou .joblib).

### 2. Tester l’inférence du modèle
etape qui consiste à verifier  comment le model entainé applique ce qu'il a appris 
- Effectuer un test de prédiction unique pour valider le bon fonctionnement du modèle.
- Mettre en place un test de prédictions par lot (un ensemble d'observation) afin d’évaluer les performances du modèle sur plusieurs entrées.

### 3. Construire l’application Streamlit
- Développer une interface web conviviale avec Streamlit.
- L’application doit permettre aux utilisateurs d’interagir avec le modèle pour effectuer des prédictions, en prenant en charge à la fois des entrées uniques et par lot.

### 4. Écrire le Dockerfile et construire l’image Docker
- Créer un Dockerfile pour définir l’environnement et les dépendances du conteneur.
- Construire une image Docker contenant l’application Streamlit et tous les fichiers nécessaires.

### 5. Exécuter le conteneur et tester l’application
- Utiliser l’image Docker pour exécuter un conteneur.
- Tester l’application Streamlit dans le conteneur afin de s’assurer qu’elle fonctionne comme prévu.

### 6. Arrêter et nettoyer les ressources Docker
- Arrêter le conteneur en cours d’exécution.
- Supprimer le conteneur et l’image Docker pour nettoyer l’environnement.

---

## Comment executer le projet

Ces etapes vont permettre de realiser ce projet

### Pre-requis  
1. Installer Python.
2. Installer Docker(https://www.docker.com/).
3. cloner le repo:
    ```bash

    ```
4. (Optionnel mais recommandé) Creer un environnement virtuel
    ```bash
    python -m venv .venv
    ./env/Scripts/activate
    ```
5. Installer les dépendances de `requirements.txt`
    ```bash
    pip install -r requirements.txt

6. Telecharger et installer Docker Desktop

### 1.Entrainement du modele
Lancer le script pour entrainer le modele et le sauvegarder:
```bash
python scripts/train_model.py
```

### 2. Test d'inference
Lancer le script suivant pour la prediction unique et par groube d'observation:
```bash
python scripts/test_inference.py
```

### 3. Construire une application Streamlit
Demarrer l'application Streamlit en local:
```bash
streamlit run app/app.py
```

### 4. Construire une image Docker
Creer une image Docker depuis `dokerfile`:
```bash
docker build -t ml-model-app .
```

### 5. Executer le conteneur Docker
Lancer le conteneur en utilisant l'image construite:
```bash
docker run -p 8501:8501 ml-model-app
```
Acceder à l'app Streamlit dans le navigateur à `...`

### 6. Arreter et nettoyer les resoources de Docker
1. Arreter l'execution de Docker
   ```bash
   docker ps
   docker stop <container_id>
   ```
2. Supprimer le Conteneur
```bash
   docker rm <container_id>
   ```
3. Supprimer l'image Docker
 ```bash
   docker rmi ml-model-app
   ```

---

### Caracteristiques clés
- **La Reproductibilité:** Le projet utilise Docker afin de garantir un fonctionnement solide sur différents environnements. 
- **Une structure modulaire:** en separant l'entrainement du model, l'inference et le deployement, ceci  pour permettre la clarté et la maintenabilité du modele
- **Interface conviviale :** L’application Streamlit offre un moyen simple et intuitif permettant aux utilisateurs d’interagir avec le modèle.

---

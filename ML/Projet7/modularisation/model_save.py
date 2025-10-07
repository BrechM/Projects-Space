from joblib import dump, load

def model_save(clf, scores, seuil = 0.9):
    """"
    Saves a model depending on the cv scores 
    """
    if scores.mean() > seuil:
        dump(clf, 'logistic_model.joblib') # l'extension .joblib est plus efficace que .pkl en matiere de stockage des estimateurs de sklearn
        print("Modele sauvegardé")

    else:
        print("Le modele n'a pas réussi le test de validation croisée")
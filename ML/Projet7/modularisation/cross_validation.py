from sklearn.model_selection import cross_val_score

def cross_validate(clf, x_train, y_train, cv=3):
    """
    Cross validates the model
    Returns an array of scores
    """
    scores = cross_val_score(clf, x_train, y_train, cv=cv)
    return scores

# attention aux noms donnés au module, il ne faut pas que ce soit le meme nom qu'un des sous modules
# de scikit pour eviter un conflit 
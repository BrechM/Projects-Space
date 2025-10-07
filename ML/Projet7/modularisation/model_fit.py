from sklearn.linear_model import LogisticRegression
import numpy as np 

def model_fit(x_train, y_train, max_iter = 500):
    """
    Fits the model with training data.
    Returns the fitted estimator.
    """
    class_0, class_1 = np.bincount(y_train)
    class_ratio = class_0 / class_1 

    if class_ratio > 1.25 or class_ratio < 0.8:
        clf = LogisticRegression(
            max_iter = max_iter,
            class_weight = 'balanced'
        )
    else:
        clf = LogisticRegression(max_iter=max_iter)
    
    clf.fit(x_train, y_train)
    
    return clf
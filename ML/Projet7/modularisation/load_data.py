from sklearn.datasets import load_breast_cancer

def load_data():
    """
    Loads the data and returns Numpy arrays
    """
    data = load_breast_cancer()
    x= data['data']
    y = data['target']
    return x, y 
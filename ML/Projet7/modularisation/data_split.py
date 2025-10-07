from sklearn.model_selection import train_test_split 

def data_split(x, y, test_size=0.25, random_state= 42):
    """"
    This function splits randomly in test and train sets and returns them as numpy array
    """
    x_train, x_test, y_train, y_test = train_test_split(
        x, y,
        test_size = test_size,
        random_state = random_state
    )
    return x_train, x_test, y_train, y_test
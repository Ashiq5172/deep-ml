import numpy as np

def shuffle_data(X, y, seed=None):
    if seed is not None:
        np.random.seed(seed)

    indices = np.arange(len(X))
    np.random.shuffle(indices)

    shuffle_X = []
    shuffle_y = []

    for i in indices:
        shuffle_X.append(X[i])
        shuffle_y.append(y[i])

    return np.array(shuffle_X), np.array(shuffle_y)
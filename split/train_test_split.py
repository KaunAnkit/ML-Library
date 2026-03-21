import numpy as np 

def train_test_split(X,y,test_size = 0.2 , random_seed = 42):

    if random_seed is not None:
        np.random.seed(random_seed)


    indices = np.arange(len(X))

    np.random.shuffle(indices)


    size = int((len(X) * (1 - test_size)))

    train , test = indices[:size], indices[size:]

    return X[train] , X[test] , y[train] , y[test]
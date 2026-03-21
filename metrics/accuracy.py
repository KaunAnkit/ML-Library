import numpy as np

def accuracy(y_pred,y_true):

    y_true , y_pred = np.array(y_true), np.array(y_pred)

    y_pred = (y_pred >= 0.5).astype(int)


    return np.mean(y_pred == y_true)
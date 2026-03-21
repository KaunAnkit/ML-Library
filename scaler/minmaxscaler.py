import numpy as np

class MinMaxScaler():

    def __init__(self):

        self.max = None
        self.min = None


    def x_max(self,x):

        self.max = np.max(x,axis = 0)
    
    def x_min(self,x):

        self.min = np.min(x,axis = 0)

    def fit_transform(self,x):

        x_min = self.x_min(x)
        x_max = self.x_max(x)

        return (x - x_min)/ (x_max - x_min)
    
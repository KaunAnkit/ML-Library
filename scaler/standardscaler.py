import numpy as np

class StandardScaler():

    def __init__(self):

        self.mean = None
        self.std = None

    def fit(self,x):

        self.mean = np.mean(x,axis =0)
        self.std = np.std(x, axis = 0)


    def transform(self,x):

        return (x - self.mean) / (self.std + 0.00000000000000001)   #zero div 
    
    def fit_transform(self,x):

        self.fit(x)
        return self.transform(x)
        

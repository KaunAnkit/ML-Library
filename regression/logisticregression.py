import numpy as np
from basemodel import BaseModel

class logisticregression(BaseModel):

    def __init__(self, lr=0.01, epochs=100):
        self.lr = lr
        self.epochs = epochs
        self.weight = None
        self.bias = 0

    def fit(self,x,y_true):

        n_S , n_F = x.shape

        self.weight = np.zeros(n_F)
        self.bias = 0


        for _ in range(self.epochs):

            
            z = np.dot(x,self.weight) + self.bias

            y_pred = 1 / (1 + np.exp(-z)) 



            error = (y_pred - y_true) 

            dw = 1/n_S * np.dot(x.T , error)
            db = 1/n_S * np.sum(error) 

            self.weight = self.weight - (self.lr*dw)
            self.bias = self.bias - (self.lr * db)

   

    def predict(self,x):

        z = np.dot(x,self.weight) + self.bias

        y_pred = 1 / (1 + np.exp(-z))

        return (y_pred >= 0.5).astype(int)
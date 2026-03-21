from basemodel import BaseModel
import numpy as np 

class linearregression(BaseModel):

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

            y_pred = np.dot(x,self.weight) + self.bias

            error = (y_pred - y_true) 

            dw = 1/n_S * (np.dot(np.transpose(x),error))
            db = 1/n_S * np.sum(error) 

            self.weight = self.weight - (self.lr*dw)
            self.bias = self.bias - (self.lr * db)

            

        

    def predict(self,x):

        return np.dot(x,self.weight) + self.bias
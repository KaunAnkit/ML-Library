import numpy as np

from basemodel import BaseModel

class KNNClassifier(BaseModel):

    def __init__(self, neighbour=5):
        self.neighbour = neighbour

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []

        for x in X_test:

            distances = np.sqrt(np.sum((self.X_train - x)**2, axis=1))

            indices = np.argsort(distances)[:self.neighbour]

            values = self.y_train[indices].astype(int)

            predictions.append(np.bitcount(values).argmax())

        return np.array(predictions)
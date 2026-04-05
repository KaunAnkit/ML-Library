
class Node():

    def __init__(self, feature_index,threshold,left,right,value):

        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left 
        self.right = right
        self.value = value

    
class DecesionTree:

    def __init__(self,max_depth =5):

        self.max_depth = max_depth
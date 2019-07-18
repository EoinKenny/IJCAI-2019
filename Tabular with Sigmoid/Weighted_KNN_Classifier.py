import numpy as np

from collections import Counter


class GlobalWeightedKNN:
    """
    A k-NN classifier with the option to give input weights
    It returns many predictions at once.
    """
    
    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.k = None
        self.weights = None
        self.predictions = list()
        
    def fit(self, X_train, y_train, k, weights):        
        self.X_train = X_train
        self.y_train = y_train
        self.k = k
        self.weights = weights
                
    def predict(self, testing_data):
        """
        Takes a 2d array of query cases.
        
        Returns a list of predictions for knn classifier
        """
                    
        np.fromiter((self.__helper(qc) for qc in testing_data), float)  
        return self.predictions
    
    
    def __helper(self, qc):
        neighbours = np.fromiter((self.__weighted_euclidean(qc, x) for x in self.X_train), float)
        neighbours = np.array([neighbours]).T 
        indexes = np.array([range(len(self.X_train))]).T
        neighbours = np.append(indexes, neighbours, axis=1)

        # Sort by second column - distances
        neighbours = neighbours[neighbours[:,1].argsort()]  
        k_cases = neighbours[ :self.k]
        indexes = [x[0] for x in k_cases]
        
        # Get indexes of original answer and answer with modified training labels
        y_answers = [self.y_train[int(x)] for x in indexes]
        answer = max(set(y_answers), key=y_answers.count)  # get most common value
        self.predictions.append(answer)
                 
            
    def __weighted_euclidean(self, qc, other):
        """
        Custom weighted euclidean distance
        
        returns: floating point number
        """
        
        return np.sum( ((qc - other)**2) * self.weights )
    
    
    
class LocalWeightedKNN:
    """
    A k-NN classifier with the option to give input weights
    
    This is a modified version for the naive local search algorithms. It only returns one prediction at a time.
    """
    
    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.k = None
        
    def fit(self, X_train, y_train, k):
                
        self.X_train = X_train
        self.y_train = y_train
        self.k = k
                
    def predict(self, qc, weights):
        """
        Takes a query cases.
        
        Returns a prediction for knn classifier
        """
                                    
        neighbours = np.fromiter((self.__weighted_euclidean(qc, x, weights) for x in self.X_train), float)
        neighbours = np.array([neighbours]).T 
        indexes = np.array([range(len(self.X_train))]).T
        neighbours = np.append(indexes, neighbours, axis=1)

        # Sort by second column - distances
        neighbours = neighbours[neighbours[:,1].argsort()]  
        k_cases = neighbours[ :self.k]
        indexes = [x[0] for x in k_cases]
        
        y_answers = [self.y_train[int(x)] for x in indexes]
        answer = max(set(y_answers), key=y_answers.count)  # get most common value
        
        return answer
    
    def __weighted_euclidean(self, qc, other, weights):
        """
        Custom weighted euclidean distance
        
        returns: floating point number
        """
        
        return np.sum( (qc - other)**2 * weights )
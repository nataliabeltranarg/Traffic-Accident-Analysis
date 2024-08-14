import pandas as pd
import matplotlib.pyplot  as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from abc import ABC, abstractmethod

class Metrics(ABC):
    
    def __init__(self, feature, target, train, test, model): 
        """
        Initialize Model class

        Args:
        feature (list) : List of names of feature columns (str)
        target (str): Name of the target variable
        train (pd.DataFrame): Train dataframe
        test (pd.DataFrame): Test dataframe
        model: Model that is going to be evaluated
        """
        self.feature = feature 
        self.target = target
        self.train = train.copy()
        self.test = test.copy()
        self.model = model

    @abstractmethod
    def calculate_metric(self):
        pass
  
class F1_Score(Metrics):
    def calculate_metric(self):
        """Calculate F1 score for each class on train and test data.

        Returns:
        A dictionary containing F1 scores for each class on the training and test sets.
        """
        predictions_train = self.model.predict(self.train[self.feature])
        predictions_test = self.model.predict(self.test[self.feature])

        f1_train = f1_score(self.train[self.target], predictions_train, average=None)
        f1_test = f1_score(self.test[self.target], predictions_test, average=None)

        return {
        'f1 score train category 1': f1_train[0],
        'f1 score train category 2': f1_train[1],
        'f1 score train category 3': f1_train[2],
        'f1 score train category 4': f1_train[3],
        'f1 score test category 1': f1_test[0],
        'f1 score test category 2': f1_test[1],
        'f1 score test category 3': f1_test[2],
        'f1 score test category 4': f1_test[3]
        }

class ConfusionMatrix(Metrics):
    def calculate_metric(self):
        """
        Calculate Confusion Matrix for each class on train and test data.

        Returns:
        A dictionary containing Confusion Matrix for each class on the training and test sets.
        """
        predictions_train = self.model.predict(self.train[self.feature])
        predictions_test = self.model.predict(self.test[self.feature])

        confusion_matrix_train = confusion_matrix(self.train[self.target], predictions_train)
        confusion_matrix_test = confusion_matrix(self.test[self.target], predictions_test)

        return {
        'confusion matrix train': confusion_matrix_train,
        'confusion matrix test': confusion_matrix_test
        }
    
    def cm_display(self):
        cm_display_tr = ConfusionMatrixDisplay(confusion_matrix=self.calculate_metric()['confusion matrix train'].round(3)).plot()
        cm_display_te = ConfusionMatrixDisplay(confusion_matrix=self.calculate_metric()['confusion matrix test'].round(3)).plot()


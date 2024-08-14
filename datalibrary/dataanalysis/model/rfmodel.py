import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class Model():
    
    def __init__(self, feature, target, train, test, params = None): 
        """
        Initialize Model class

        Args:
        feature (list) : List of names of feature columns (str)
        target (str): Name of the target variable
        train (pd.DataFrame): Train dataframe
        test (pd.DataFrame): Test dataframe
        params (dict): Dictionary of specified parameters, default: n_estimators=100, max_depth=None, random_state=42
        """
        self.__feature = feature # 1. Feature columns that are going to be used
        self.__target = target # 2. Target column that is going to be used
        self.__train = train.copy()
        self.__test = test.copy()
        # Set default parameters if none are provided
        default_params = {'n_estimators': 100, 'max_depth': None, 'random_state': 42}
        if params is not None:
            default_params.update(params)

        self.params = default_params
        self.model = RandomForestClassifier(**default_params)


    def model_predictions(self):
        """
        RandomForestClassifier predictions for train and test

        Returns:
        Train and test pd.DataFrame with prediction column
        """
        self.model.fit(self.__train[self.__feature], self.__train[self.__target])

        predictions_train = self.model.predict_proba(self.__train[self.__feature])
        predictions_train = pd.DataFrame(predictions_train, index = self.__train.index, columns=[f'pred_{i}' for i in range(1,5)])
        train = pd.concat([self.__train, predictions_train], axis = 1)

        predictions_test = self.model.predict_proba(self.__test[self.__feature])
        predictions_test = pd.DataFrame(predictions_test, index = self.__test.index, columns=[f'pred_{i}' for i in range(1,5)])
        test = pd.concat([self.__test, predictions_test], axis = 1)

        return train, test


    def randomized_param_tuning(self):
        """
        Randomized Parameter Tuning for Random Forest Classifier
        
        Parameter grid:
        n_estimators: Number of trees in random forest
        max_features: Number of features to consider at every split
        max_depth: Maximum number of levels in tree
        min_samples_split: Minimum number of samples required to split a node
        min_samples_leaf: Minimum number of samples required at each leaf node
        bootstrap: method of secelcting samples for training each tree

        Returns: Best parameters (dict)
        """
        model = self.model
        n_estimators = [5,20,50,100] # Number of trees in random forest
        max_features = ['log2', 'sqrt'] # Number of features to consider at every split
        max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]  # Maximum number of levels in tree
        max_depth.append(None)
        min_samples_split = [2, 5, 10] # Minimum number of samples required to split a node
        min_samples_leaf = [1, 2, 4]  # Minimum number of samples required at each leaf node
        bootstrap = [True, False] # Method of selecting samples for training each tree
        random_grid = {'n_estimators': n_estimators,
                'max_features': max_features,
                'max_depth': max_depth,
                'min_samples_split': min_samples_split,
                'min_samples_leaf': min_samples_leaf,
                'bootstrap': bootstrap}
        rf_random = RandomizedSearchCV(estimator = model, param_distributions = random_grid, n_iter = 20, cv = 3, verbose=2, random_state=42, n_jobs = -1)
        # Fit the random search model
        rf_random.fit(self.__train[self.__feature], self.__train[self.__target])
        return rf_random.best_params_

    def grid_search_tuning(self):
        """
        GirdSearch Parameter Tuning for Random Forest Classifier
        
        Parameter grid:
        n_estimators: Number of trees in random forest
        max_features: Number of features to consider at every split
        max_depth: Maximum number of levels in tree
        min_samples_split: Minimum number of samples required to split a node
        min_samples_leaf: Minimum number of samples required at each leaf node
        bootstrap: method of secelcting samples for training each tree

        Returns: Best parameters (dict)
        """
        model = self.model
        n_estimators = [10,50,100] # Number of trees in random forest
        max_features = ['log2', 'sqrt'] # Number of features to consider at every split
        max_depth = [None, 10, 20]  # Maximum number of levels in tree
        max_depth.append(None)
        min_samples_split = [2, 5, 10] # Minimum number of samples required to split a node
        min_samples_leaf = [1, 2, 4]  # Minimum number of samples required at each leaf node
        bootstrap = [True, False] # Method of selecting samples for training each tree
        random_grid = {'n_estimators': n_estimators,
                'max_features': max_features,
                'max_depth': max_depth,
                'min_samples_split': min_samples_split,
                'min_samples_leaf': min_samples_leaf,
                'bootstrap': bootstrap}
        rf_grid = GridSearchCV(estimator = model, param_grid = random_grid, cv = 2, verbose=2, n_jobs = -1)
        # Fit the random search model
        rf_grid.fit(self.__train[self.__feature], self.__train[self.__target])
        return rf_grid.best_params_



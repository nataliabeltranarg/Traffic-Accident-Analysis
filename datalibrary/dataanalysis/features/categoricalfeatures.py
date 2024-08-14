import pandas as pd
import numpy as np

def one_hot_encoding(data, column):
    """ 
    perform one hot encoding on a given (multicategorical) column, 
    creates a column for each category with binary values (1 or 0), 
    drops original column

    Args:
        data (DataFrame) : whole dataset
        column (list) : list of strings with column names that action will be performed on

    Returns:
        DataFrame
    """
    data = data.copy() # create deep copy of data

    dummy = pd.get_dummies(data[column]) # get dummies
    data = pd.concat([data, dummy], axis=1) # add dummy columns to dataframe 
    data = data.drop(columns = column)

    return data

def binary_var(data, column):
    """ 
    creates binary column with values 0 or 1 for given column,
    drops original column

    Args:
        data (DataFrame) : whole dataset
        column (str) : column name that action will be performed on

    Returns:
        DataFrame
    """

    data = data.copy() # create deep copy of data

    dummy = pd.get_dummies(data[column], drop_first=True) # get dummies
    data = pd.concat([data, dummy], axis=1) # add dummy columns to dataframe 
    data = data.drop(columns = column)

    return data

def binning(data, column, bins, labels):
    """ 
    transform numerical column into categorical bins respecting threshold values and bin labels 

    Args:
        data (DataFrame) : whole dataset
        column (str) : column name that action will be performed on
        bins (list): list of integers corresponding to thresholds for bins
        labels (list): list of strings corresponding to name/labels of bins

    Returns:
        DataFrame
    """

    data = data.copy() # create deep copy of data

    data[column + 'bin'] = pd.cut(data[column], bins=bins, labels=labels)
    data.drop(columns=column, inplace=True)
    return data

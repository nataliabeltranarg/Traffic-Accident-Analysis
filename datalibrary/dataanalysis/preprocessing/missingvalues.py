import pandas as pd
import numpy as np

def drop_row_na(data, column:list):
    """ Drop entire rows containing NaNs in the column given 
    Args:
        data (DataFrame) : whole dataset
        column (list): column to perform action on
    Returns:
        DataFrame
    """
    data = data.copy()
    for col in column:
        data.dropna(subset=[col], inplace=True)
    return data

def fill_na_mean(data, column:list):
    """ Fill NaNs in the column given with the mean of this column
    Args:
        data (DataFrame) : whole dataset
        column (list): column to perform action on
    Returns:
        DataFrame
    """
    data = data.copy() # create deep copy of data
    for col in column:
        data[col].fillna(data[col].mean(), inplace=True) 
    return data

def fill_na_0(data, column:list):
    """ Fill NaNs in the column given with 0 
    Args:
        data (DataFrame) : whole dataset
        column (list): column to perform action on
    Returns:
        DataFrame
    """
    data = data.copy() # create deep copy of data
    for col in column:
        data[col].fillna(0, inplace=True) 
    return data

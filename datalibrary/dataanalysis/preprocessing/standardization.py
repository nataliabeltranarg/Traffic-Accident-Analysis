import pandas as pd
import numpy as np

def standardize(data, columns):
    """ 
    standardize given columns by subtracting the mean and dividing by standard deviation

    Args:
        data (DataFrame) : whole dataset
        column (list) : list of strings with column names that action will be performed on

    Returns:
        DataFrame
    """

    data = data.copy() # create deep copy of data

    for column in columns:
        data[column + '_standardized'] = (data[column] - data[column].mean()) / data[column].std()
        
    # Drop the original columns
    data.drop(columns=columns, inplace=True)
    return data

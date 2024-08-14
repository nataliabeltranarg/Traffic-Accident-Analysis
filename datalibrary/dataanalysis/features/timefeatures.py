import pandas as pd
import numpy as np

def time_difference(data, end_col, start_col):
    """ get difference of two date time columns to compute length of time
    
    Args: 
        data (DataFrame): whole dataset
        end_col (str): name of column with end times in datetime format
        start_col (str): name of column with start times in datetime format

    Returns: 
        DataFrame
    """
    data = data.copy()
    data['Length_Time'] = data[end_col] - data[start_col]
    data['Length_Time_Hours'] = data['Length_Time'].dt.total_seconds()/60/60 # hours # need to remove outliers

    return data

def get_month(data, column): 
    """ extract month from a datetime column
    
    Args: 
        data (DataFrame): whole dataset
        column (str): name of column with times in datetime format

    Returns: 
        DataFrame
    """
    data = data.copy()

    new_col = 'Month_' + column
    data[new_col] = data[column].dt.month

    return data

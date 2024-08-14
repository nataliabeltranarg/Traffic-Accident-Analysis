import pandas as pd
import numpy as np

def time_type(data, column):
    """ convert column with times in standard format to datetime type

    Args: 
        data (DataFrame): whole dataset
        column (str) : name of column with strings following datatime format

    Returns: 
        DataFrame
    
    """
    data = data.copy()
    data.loc[data[column].str.len() > 19, column] = data[column].str.replace('.000000000', '')
    data.loc[data[column].str.len() > 19, column] = data[column].str.replace('.000000', '')

    data[column] =  pd.to_datetime(data[column], utc=True)
    return data
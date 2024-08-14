import pandas as pd
import numpy as np

def winsorize(data, column):
    """ 
    winsorizing given column: values below 0.01 quantile are replaced by that value and 
    values above 0.99 quantile are replaced by that value

    Args:
        data (DataFrame) : whole dataset
        column (str) : column name that action will be performed on

    Returns:
        DataFrame
    """

    data = data.copy() # create deep copy of data

    # Calculate the 1st and 99th percentiles
    first_percentile = data[column].quantile(0.01)
    ninety_ninth_percentile = data[column].quantile(0.99)

    #print(len(data[data[column] > ninety_ninth_percentile]))

    # Windsorize the 'num_rooms' column
    data[column] = data[column].apply(lambda x: first_percentile if x < first_percentile else (ninety_ninth_percentile if x > ninety_ninth_percentile else x))

    #print(len(data[data[column] > ninety_ninth_percentile]))

    return data

import pandas as pd
import numpy as np

def road_feature_sum(data, columns):
    """
    Sum the number of True values for certain road features.

    Args:
        data (DataFrame) : whole dataset
        columns (list): List of column names (str) to be used

    Returns:
        DataFrame with the column of sums
    """

    data = data.copy()

    selected_data = data[columns] # Select the specified columns

    data['Road_Feature_Sum'] = np.sum(selected_data == True, axis=1) # Count the number of True values in each row
    return data

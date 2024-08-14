import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(data):
    """ Split data intro train and test dataframes

    Args:
        data (DataFrame) : dataframe to split into train and test

    Returns:
        tuple: (DataFrame, DataFrame)
    """

    train, test = train_test_split(data, test_size=0.2)
    return train, test

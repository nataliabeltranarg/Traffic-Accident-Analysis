import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path): 
    """ Load data from a csv file

    Args:
        file_path (str) : file path of dataframe (in csv format) to load

    Returns:
        DataFrame
    """

    df = pd.read_csv(file_path)
    return df

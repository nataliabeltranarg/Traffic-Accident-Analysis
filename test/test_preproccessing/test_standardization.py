from dataanalysis.preprocessing import standardization
import pandas as pd
import pytest 

###### standardize FUNCTION ######

def test_standardize_mean():
    """
    Test that the mean of the standardized colums is aprox. 0
    """
    test_data = pd.DataFrame({'A': [1, 2, 3, 4],'B': [5, 4, 3, 2]})
    standardized_data = standardization.standardize(test_data, ['A', 'B'])

    assert all(abs(standardized_data.mean()) < 1e-10)

def test_standardize_std():
    """
    Test that the standard deviation of the standardized colums is aprox. 1
    """
    test_data = pd.DataFrame({'A': [1, 2, 3, 4],'B': [5, 4, 3, 2]})
    
    standardized_data = standardization.standardize(test_data, ['A', 'B'])
    assert all(abs(standardized_data.std() - 1) < 1e-10)


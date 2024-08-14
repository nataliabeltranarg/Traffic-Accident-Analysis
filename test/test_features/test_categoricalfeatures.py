from dataanalysis.features import categoricalfeatures
import pandas as pd
import numpy as np
import pytest

###### one_hot_encoding FUNCTION ######

# Create sample data for onehotencoding & binary test
@pytest.fixture
def data_sample_onehot_binary():
    data = pd.DataFrame({'City': ["London", "Cambridge","Liverpool"],
            'Transportation': ["car", "car", "bus"],
            'Value': [20, 10, 30]})
    return data

# test that the encoding is done correctly
def test_one_hot_encoding(data_sample_onehot_binary):
    # one_hot_encoding(data, column)
    output = categoricalfeatures.one_hot_encoding(data_sample_onehot_binary, 'City')
    expected_output = {'London', 'Cambridge', 'Liverpool', 'Transportation','Value'}
    assert set(output.columns) == expected_output

# test that the column has been dropped 
def test_one_hot_encoding_drop_column(data_sample_onehot_binary):
    output = categoricalfeatures.one_hot_encoding(data_sample_onehot_binary, 'Transportation')
    expected_output = 'Transportation'
    assert expected_output not in output

###### binary_var FUNCTION ######
# test that the binvary is done correctly
def test_binary(data_sample_onehot_binary):
    # binary_var(data, column)
    output = categoricalfeatures.binary_var(data_sample_onehot_binary, 'City')
    expected_output = {'London', 'Liverpool', 'Transportation','Value'}
    assert set(output.columns) == expected_output

# test that the column has been dropped 
def test_binary_drop_column(data_sample_onehot_binary):
    output = categoricalfeatures.binary_var(data_sample_onehot_binary, 'Transportation')
    expected_output = 'Transportation'
    assert expected_output not in output

###### binning FUNCTION ######
# test that function returns a dataframe object and right values
def test_binning(): 
    d = {'col1': [3, 1, 0, 3], 'col2': [0, 5, 1, 0]}
    x = pd.DataFrame(data=d, index=[0, 1, 2, 3])
    output = categoricalfeatures.binning(x, 'col2', [-1, 2, 10], ['low', 'high'])
    expected_output = pd.DataFrame(data={'col1': [3, 1, 0, 3], 'col2bin': ['low', 'high', 'low', 'low']})
    assert type(output) == type(expected_output)
    assert (output['col2bin'].values == expected_output['col2bin'].values).all()
    assert output.shape == expected_output.shape

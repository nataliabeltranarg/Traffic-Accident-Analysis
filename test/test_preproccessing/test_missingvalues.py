from dataanalysis.preprocessing import missingvalues
import pandas as pd
import pytest 

###### drop_row_na FUNCTION ######
def test_drop_row_na(): 
    d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
    x = pd.DataFrame(data=d, index=[0, 1, 2, 3])
    output = missingvalues.drop_row_na(x, ['col2'])
    expected_output = pd.DataFrame(data={'col1': [2, 3], 'col2': pd.Series([2, 3])})
    # check shape
    assert output.shape == expected_output.shape
    # check that its a dataframe
    assert type(output) == type(expected_output)
    # check values in column 1 and 2
    assert (output['col1'].values == expected_output['col1'].values).all()
    assert (output['col2'].values == expected_output['col2'].values).all()

##### fill_na_mean FUNCTION ######
def fill_na_mean(): 
    d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
    x = pd.DataFrame(data=d, index=[0, 1, 2, 3])
    output = missingvalues.fill_na_mean(x, ['col2'])
    expected_output = pd.DataFrame(data={'col1': [0, 1, 2, 3], 'col2': [2.5, 2.5, 2, 3]})
    assert output.shape == expected_output.shape
    assert type(output) == type(expected_output)
    assert (output['col1'].values == expected_output['col1'].values).all()
    assert (output['col2'].values == expected_output['col2'].values).all()

###### fill_na_0 FUNCTION ######
def test_fill_na_0(): 
    d = {'col1': [0, 1, 2, 3], 'col2': pd.Series([2, 3], index=[2, 3])}
    x = pd.DataFrame(data=d, index=[0, 1, 2, 3])
    output = missingvalues.fill_na_0(x, ['col2'])
    expected_output = pd.DataFrame(data={'col1': [0, 1, 2, 3], 'col2': [0, 0, 2, 3]})
    assert output.shape == expected_output.shape
    assert type(output) == type(expected_output)
    assert (output['col1'].values == expected_output['col1'].values).all()
    assert (output['col2'].values == expected_output['col2'].values).all()

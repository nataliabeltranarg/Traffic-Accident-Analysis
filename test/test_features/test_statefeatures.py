from dataanalysis.features import statefeatures
import pandas as pd
import numpy as np
import pytest

###### state_to_region FUNCTION ######
### note: column has to be called State

# test that function returns object with the right shape, type and values
def test_state_to_region_shape(): 
    d = {'col1': [3, 1, 0, 3], 'State': ['CA', 'NY', 'NJ', 'NV']}
    x = pd.DataFrame(data=d, index=[0, 1, 2, 3])
    output = statefeatures.state_to_region(x, 'State') 
    expected_output = pd.DataFrame(data={'col1': [3, 1, 0, 3], 'State': ['CA', 'NY', 'NJ', 'NV'], 'Region': ['west', 'northeast', 'northeast', 'west']})
    assert output.shape == expected_output.shape
    assert type(output) == type(expected_output)
    assert (output['Region'].values == expected_output['Region'].values).all()


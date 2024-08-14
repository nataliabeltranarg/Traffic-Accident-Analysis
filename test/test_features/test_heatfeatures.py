from dataanalysis.features import heatfeatures
import pandas as pd
import numpy as np
import pytest

## Temperature Conversion Function ##

def test_temperature_conversion_column_names():
    data = pd.DataFrame({'Temperature_1(F)': [32, 212, 50, 77],
                         'Temperature_2(F)': [-10, 14, 32, 50]})
    
    result = heatfeatures.temperature_conversion(data, ['Temperature_1(F)', 'Temperature_2(F)'])
    
    assert 'Temperature_1(F)' not in result.columns
    assert 'Temperature_2(F)' not in result.columns
    assert 'Temperature_1(C)' in result.columns
    assert 'Temperature_2(C)' in result.columns


## Heat Index Function ##
@pytest.fixture
def data_sample_heat_index():
    data2 = {'temp': [65, 87, 95, 60, 65, 72, 84, 75, 91, 100, 112,104], 
            'humidity': [54, 78, 100,77, 62, 81, 94, 102, 66, 55, 63, 82],
            }
    return pd.DataFrame(data2)

# test that the new column is created 
def test_heat_index_f_column(data_sample_heat_index):
    data =data_sample_heat_index.copy()
    output = heatfeatures.heat_index_f(data_sample_heat_index, 'temp' , 'humidity')
    expected_output = {'temp', 'humidity' , 'Heat_Index(F)'}
    assert set(output.columns) == expected_output
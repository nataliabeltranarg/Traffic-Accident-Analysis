from dataanalysis.features import timefeatures
import pandas as pd
import numpy as np
import pytest
from datetime import datetime


###### get_month FUNCTION ######

# test that function returns object with the right shape, type, values
def test_get_month_shape(): 
    d = {'col1': [1, 1], 'Time': [datetime(2022, 12, 28, 23, 55, 59), datetime(2016, 1, 28, 14, 21, 30)]}
    x = pd.DataFrame(data=d, index=[0, 1])
    output = timefeatures.get_month(x, 'Time') 
    expected_output = pd.DataFrame(data={'col1': [1, 1], 'Time': [datetime(2022, 12, 28, 23, 55, 59), 
                                                                  datetime(2016, 1, 28, 14, 21, 30)], 'Month_Time': [12, 1]})
    assert output.shape == expected_output.shape
    assert type(output) == type(expected_output)
    assert (output['Time'].values == expected_output['Time'].values).all()

###### Time Difference FUNCTION ######
# Create sample data for the time_difference test
@pytest.fixture
def data_sample_time_difference():
    data = pd.DataFrame({'start': [datetime(2023, 1, 12, 6, 48, 32),  datetime(2023, 2, 28, 12, 58, 0)],
            'end': [datetime(2023, 12, 22, 5, 39, 8), datetime(2023, 3, 16, 23, 27, 7)]
            })
    return data

# testing that the 'Length_Time' column has been created after running function 
def test_time_difference_column_time(data_sample_time_difference):
    start_col = 'start'
    end_col = 'end'
    output = timefeatures.time_difference(data_sample_time_difference, end_col, start_col)
    expected_output = 'Length_Time'
    assert expected_output in output.columns

# testing that the 'Length_Time_Hours' column has been created after running function 
def test_time_difference_column_time_hours(data_sample_time_difference):
    start_col = 'start'
    end_col = 'end'
    output = timefeatures.time_difference(data_sample_time_difference, end_col, start_col)
    expected_output = 'Length_Time_Hours'
    assert expected_output in output.columns

# testing the that the length time calculation is done correctly
def test_time_difference_time_subtraction(data_sample_time_difference):
    start_col = 'start'
    end_col = 'end'
    output = timefeatures.time_difference(data_sample_time_difference, end_col, start_col)
    expected_output = data_sample_time_difference[end_col] - data_sample_time_difference[start_col]
    assert (output['Length_Time'] == (expected_output)).all()

# testing the conversion of length time to hours is done correctly
def test_time_difference_conversion_hours(data_sample_time_difference):
    start_col = 'start'
    end_col = 'end'
    output = timefeatures.time_difference(data_sample_time_difference, end_col, start_col)
    expected_output = (data_sample_time_difference[end_col] - data_sample_time_difference[start_col]).dt.total_seconds()/60/60
    assert (output['Length_Time_Hours'] == (expected_output)).all()

from dataanalysis.preprocessing import timedata
import pandas as pd
import pytest 

### Time Type Function #### 
# sample data for time type function 
@pytest.fixture
def data_sample_time_type():
    data = pd.DataFrame({'DateTime': [ '2023-01-12 11:23:08', '2023-07-01 15:30:43', '1996-03-16 22:45:10']})
    return data

def test_time_type_conversion(data_sample_time_type):
    output = timedata.time_type(data_sample_time_type, 'DateTime')
    expected_output = ['2023-01-12 11:23:08+00:00', '2023-07-01 15:30:43+00:00', '1996-03-16 22:45:10+00:00']
    assert output['DateTime'].astype(str).tolist() == expected_output

def test_time_type_dtypes(data_sample_time_type):
    output = timedata.time_type(data_sample_time_type, 'DateTime')
    expected_output = 'datetime64[ns, UTC]'
    assert output['DateTime'].dtypes == expected_output


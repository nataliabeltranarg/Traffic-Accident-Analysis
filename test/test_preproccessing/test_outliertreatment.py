from dataanalysis.preprocessing import outliertreatment
import pandas as pd
import pytest 

###### winsorize FUNCTION ######
#sample data test winsorize function
@pytest.fixture
def data_sample_winsorize():
    data = pd.DataFrame({'Numbers': [20,10,30, 9, 45,2, 7, 100, 3000, 56, 77, 85, 9, 95, 64, 32, 11]})
    return data

# Test winsorize first percentile
def test_winsorize_first(data_sample_winsorize):
    output = outliertreatment.winsorize(data_sample_winsorize, 'Numbers')
    expected_output = data_sample_winsorize['Numbers'].quantile(0.01)
    assert all(output == expected_output)

# Test winsorize ninety_ninth_percentile 
def test_winsorize_ninety(data_sample_winsorize):
    output = outliertreatment.winsorize(data_sample_winsorize, 'Numbers')
    expected_output = data_sample_winsorize['Numbers'].quantile(0.99)
    assert all(output == expected_output)


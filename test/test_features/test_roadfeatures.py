from dataanalysis.features import roadfeatures, statefeatures, timefeatures
import pandas as pd
import numpy as np
import pytest

###### Sum of road features FUNCTION ######

def test_road_feature_sum_result():
    data = pd.DataFrame({
    'Speed_Bump': [True, False, True, False],'Crosswalk': [False, True, False, True],
    'Roundabout': [True, True, True, False]})
    result = roadfeatures.road_feature_sum(data, ['Speed_Bump', 'Crosswalk', 'Roundabout'])
    expected_sum = [2, 2, 2, 1]
    assert all(result['Road_Feature_Sum'] == expected_sum)

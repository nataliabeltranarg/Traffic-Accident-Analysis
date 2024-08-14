import pandas as pd
import numpy as np

def temperature_conversion(data, columns):
    """ 
    Convert temperature from Fahrenheit to Celsius

    Args:
        data (DataFrame) : whole dataset
        column (list) : List of the columns with temperature in Fahrenheit

    Returns:
        DataFrame with overwritten temperature column
    """

    data = data.copy()
    
    for col in columns:
        data[col] = [(5/9) * (F - 32) for F in data[col]]
        if '(F)' in col:
            new_col_name = col.replace('(F)', '(C)')
        else: 
            new_col_name = col + '(C)'
        data.rename(columns={col: new_col_name}, inplace=True)

    return data

def heat_index_f(data, temp, humidity):
    """ use relative humidity (%) and temperature (f) to calculate heat index
    calculations based on: https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml

    Args: 
        data (DataFrame): whole dataset
        temp (str): name of column with temperature in F
        humidity (str): name of column with humidity in %

    Returns: 
        DataFrame
    """
    data = data.copy()
    
    T = data[temp]
    RH = data[humidity]

    # baseline formula
    data['Heat_Index(F)'] = -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH

    # different adjustements
    data.loc[(data[humidity]<13) & (data[temp]>80) & (data[temp]<110),'Heat_Index(F)'] = data['Heat_Index(F)'] - ((13-data[humidity])/4) * np.sqrt(np.absolute(17 - abs(data[temp] - 95))/ 17)
    data.loc[(data[humidity]>85) & (data[temp]>80) & (data[temp]<87), 'Heat_Index(F)'] = data['Heat_Index(F)'] - ((data[humidity]-85)/10) * ((87-data[temp])/5)
    data.loc[(data['Heat_Index(F)']<80), 'Heat_Index(F)'] = 0.5 * (data[temp] + 61.0 + ((data[temp]-68.0)*1.2) + (data[humidity]*0.094))

    return data
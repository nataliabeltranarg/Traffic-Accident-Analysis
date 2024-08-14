import pandas as pd
import numpy as np

def state_to_region(data, column):
    """ organize US states into regions 

    Args:
        data (DataFrame) :  whole dataset
        column (list) : column with US state abbreviations
    
    Returns:
        DataFrame
    """
    data = data.copy()

    state = {0: 'AL', 1: 'AK', 2: 'AZ', 3: 'AR', 4: 'CA', 5: 'CO', 6: 'CT', 7: 'DE', 8: 'FL', 9: 'GA', 
            10: 'HI', 11: 'ID', 12: 'IL', 13: 'IN', 14: 'IA', 15: 'KS', 16: 'KY', 17: 'LA', 18: 'ME', 
            19: 'MD', 20: 'MA', 21: 'MI', 22: 'MN', 23: 'MS', 24: 'MO', 25: 'MT', 26: 'NE', 27: 'NV', 
            28: 'NH', 29: 'NJ', 30: 'NM', 31: 'NY', 32: 'NC', 33: 'ND', 34: 'OH', 35: 'OK', 36: 'OR', 
            37: 'PA', 38: 'RI', 39: 'SC', 40: 'SD', 41: 'TN', 42: 'TX', 43: 'UT', 44: 'VT', 45: 'VA', 
            46: 'WA', 47: 'WV', 48: 'WI', 49: 'WY'}
    
    region = {0: 'southeast', 1: 'west', 2: 'southwest', 3: 'southeast', 4: 'west', 5: 'west', 6: 'northeast', 
            7: 'southeast', 8: 'southeast', 9: 'southeast', 10: 'west', 11: 'west', 12: 'midwest', 13: 'midwest', 
            14: 'midwest', 15: 'midwest', 16: 'southeast', 17: 'southeast', 18: 'northeast', 19: 'southeast', 
            20: 'northeast', 21: 'midwest', 22: 'midwest', 23: 'southeast', 24: 'midwest', 25: 'west', 26: 'midwest', 
            27: 'west', 28: 'northeast', 29: 'northeast', 30: 'southwest', 31: 'northeast', 32: 'southeast', 
            33: 'midwest', 34: 'midwest', 35: 'southwest', 36: 'west', 37: 'northeast', 38: 'northeast', 39: 'southeast', 
            40: 'midwest', 41: 'southeast', 42: 'southwest', 43: 'west', 44: 'northeast', 45: 'southeast', 46: 'west', 
            47: 'southeast', 48: 'midwest', 49: 'west'}

    state_df = pd.DataFrame.from_dict({'State': state, 'Region': region})
    data = data.merge(state_df, how = 'left', on = column)

    return data
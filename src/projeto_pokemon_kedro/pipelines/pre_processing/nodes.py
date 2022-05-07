"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.0
"""

import pandas as pd

def pre_processing(df:pd.DataFrame, selected_generation=[1]):
    """
    Function to clean the data (drop the unused columns and drop NaN values)

        Args: pokemon raw dataset
        Returns: pre_processed data

    """
    #Remove unused columns
    df = df.drop(columns=['type2','pokedex_number'])
    
    #Remove null valous
    df = df.dropna()
    
    #Select Generation
    df = df[df.generation.isin(selected_generation)]
    
    return df

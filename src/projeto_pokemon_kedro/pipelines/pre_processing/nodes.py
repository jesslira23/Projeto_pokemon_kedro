"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.0
"""

import pandas as pd

def pre_processing(df):
    """
    Function to clean the data (drop the unused columns and drop NaN values)

        Args: pokemon raw dataset
        Returns: pre_processed data

    """
    df = df.drop(columns=['type2'])
    df = df.dropna()
    return df
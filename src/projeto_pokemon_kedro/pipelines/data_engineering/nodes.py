"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

import pandas as pd
import ast
from sklearn.preprocessing import LabelEncoder

def enconde_target_variable(df):
    label_encoder = LabelEncoder()
    label_encoder = label_encoder.fit(df['type1'])

    df['type1'] = label_encoder.transform(df['type1'])

    return df, label_encoder



def calculate_number_of_abilities(df):
    """
        Helper function for determining pokemon's numeber of ablities
    """

    abilities = ast.literal_eval(df['abilities'])
    number_of_abilities = len(abilities)

    return number_of_abilities


def create_number_of_abilities_feature(df):
    """"
        Adds abilities feature column to dataframe 
    """
    
    df = df.assign(
        number_of_abilities = df.apply(
            calculate_number_of_abilities,
            axis=1
        )
    )

    # List columns with against variables
    against_cols = [col for col in df if col.startswith('against')]

    # Select numerical columns
    numerical_starts_columns = [
    'base_total', 'attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed', 'height_m', 'weight_kg', 'number_of_abilities'
    ]

    #Creature final column list 
    cols_to_select = against_cols + numerical_starts_columns + ['type1']


    #Select columns
    df = df[cols_to_select]

    return df
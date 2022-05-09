"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def enconde_target_variable(df):
    label_encoder = LabelEncoder()
    label_encoder = label_encoder.fit(df['type1'])

    df['type1'] = label_encoder.transform(df['type1'])

    return df, label_encoder
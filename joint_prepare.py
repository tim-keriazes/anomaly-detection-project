import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


#Dropping columns with an inordinate number of nulls (rendering variable essentially useless)
def drop_columns(df):
    df = df.drop(columns = [
        'updated_at',
        'deleted_at',
        'slack',
        'id'
    ],
    axis=1)
    return df


def handle_nulls(df):    
    # We keep % of the data after dropping nulls
    # round(df.dropna().shape[0] / df.shape[0], 4) returned ...
    df = df.dropna()
    return df
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


def create_ancillary_df(df):
    # In order to drop nulls, we save rows with nulls in separate df
    df_admin = df[df.program_id.isnull()]
    return df


def handle_nulls(df):    
    # We keep 95% of the data after dropping nulls
    # round(df.dropna().shape[0] / df.shape[0], 4) returned ...
    df = df.dropna()
    return df


def prepare_logs(df):
    '''
    Drops unnecessary columns
    Separates nulls into separate df
    Handles Nulls
    '''

    df = drop_columns(df)

    df_admin = create_ancillary_df(df)

    df = handle_nulls(df)

    return df, df_admin
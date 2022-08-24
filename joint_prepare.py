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
    return df_admin


def handle_nulls(df):    
    # We keep 95% of the data after dropping nulls
    # round(df.dropna().shape[0] / df.shape[0], 4) returned ...
    df = df.dropna()
    return df


def parse_path(path):
    parts = path.split("/")
    output = {}
    if len(parts) == "/":
        output['primary_topic'] = 'None'
        output['subtopic'] = 'None'
        output['tertiary'] = 'None'  
    elif len(parts) == 1:
        output['primary_topic'] = parts[0]
        output['subtopic'] = 'None'
        output['tertiary'] = 'None'
    elif len(parts) == 2:
        output['primary_topic'] = parts[0]
        output['subtopic'] = parts[1]
        output['tertiary'] = 'None'
    else: 
        output['primary_topic'] = parts[0]
        output['subtopic'] = parts[1]
        output['tertiary'] = parts[2]
    return pd.Series(output)
    

def apply_path(df):
    #
    tf = df.path.apply(parse_path)
    df = df.merge(tf, how = 'inner', left_index = True, right_index = True)
    return df


def prepare_logs(df):
    '''
    Drops unnecessary columns
    Separates nulls into separate df
    Handles Nulls
    splits path, parses into components
    '''

    df = drop_columns(df)

    df_admin = create_ancillary_df(df)

    df = handle_nulls(df)

    df = apply_path(df)
    
    return df, df_admin
# https://www.codewars.com/kata/5e60cdcd01712200335bd676

import pandas as pd

def rename_columns(df, names):  
    headers = df.columns
    return  df.rename(columns={f:t for f,t in zip(headers, names)}, inplace=False)

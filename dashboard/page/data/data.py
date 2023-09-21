import pandas as pd

df = pd.read_csv('order_payments_dataset.csv')

def getDataFrame() -> pd.DataFrame:
    return df.loc[:, df.columns != 'order_id']
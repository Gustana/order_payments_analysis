import pandas as pd

def getDataFrame(dataset_path:str) -> pd.DataFrame:
    df = pd.read_csv(dataset_path)
    return df.loc[:, df.columns != 'order_id']
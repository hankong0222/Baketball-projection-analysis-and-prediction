import numpy as np
import pandas as pd

def data_preprocess(df):
    data = df.copy()

    data['hght'] = data.groupby('pid')['hght'].transform(
        lambda x: x.fillna(x.mean())
    )
    
    data.drop(columns=["pid","fnm", "lnm"], inplace=True)

    motion_cols = [
        't','cx','cy','cz',
        'cvx','cvy','cvz',
        'cax','cay','caz'
    ]

    data[motion_cols] = data[motion_cols].interpolate()

    data = data.drop(columns=['cv','ca','d'])

    data.dropna(inplace=True)

    return data

if __name__ == "__main__":
    df = pd.read_csv("data/raw/path_detail.csv")
    processed_data = data_preprocess(df)
    processed_data.to_csv("data/processed/processed_path_detail.csv", index=False)
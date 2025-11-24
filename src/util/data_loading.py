# file for data loading and preprocessing

from pathlib import Path
import pandas as pd
import numpy as np

cwd = Path().cwd()
project_folder = cwd.parent

def load_raw_data(file_name):
    data_path = Path(f'data/{file_name}')
    file = project_folder.joinpath(data_path)

    print("Looking for file at:", file.resolve())
    if not file.exists():
        raise FileNotFoundError(f"Dataset file not found: {file}")

    df = pd.read_csv(file)
    return df

def convert_nan_zero(df):
    pass

def clean_median(df):
    df["Mon-Yr"] = pd.to_datetime(df["Mon-Yr"], format='%b-%y')

    cols = df.columns.drop("Mon-Yr")

    df[cols] = (
        df[cols]
        .replace({r'\$': '', ',': '', '--': '', '—': '', 'N/A': '', 'null': ''}, regex=True)
        .replace('', np.nan)
        .astype(float)
    )

    df.fillna(0, inplace=True)
    return df




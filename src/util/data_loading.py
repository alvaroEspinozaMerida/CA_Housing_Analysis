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

def clean_dates(df):

    df[['yy', 'q']] = df['quarter'].str.extract(r'(\d{2}):Q([1-4])')
    df['yy'] = df['yy'].astype(int)

    df['year'] = df['yy'].apply(lambda y: 2000 + y if y <= 24 else 1900 + y)

    df['quarter'] = pd.PeriodIndex(df['year'].astype(str) + 'Q' + df['q'], freq='Q')

    df['quarter_start'] = df['quarter'].dt.to_timestamp()

    df = df[df['year'] > 1990]

    return df

def combine_debt(df1,df2):
    debt_all = pd.concat(
        [df2, df1],
        axis=0,  # stack rows
        ignore_index=True
    )

    cols = ['Mortgage', 'HE Revolving', 'Auto Loan', 'Credit Card',
       'Other', 'Total']   # pick your columns

    debt_all[cols] = debt_all[cols].astype(float)

    return debt_all


def get_debt(df, category):
    col = [category, "quarter_start"]
    new_df = df[col].copy()
    new_df = new_df[new_df["quarter_start"].dt.month == 10].copy()
    new_df["Year"] = new_df["quarter_start"].dt.year

    new_df.drop("quarter_start", axis=1, inplace=True)

    return new_df


def get_median_prices(df,area):
    #extract median prices for a specific area in format where year is a column
    # median = load_raw_data('MedianPricesofExistingDetachedHomesHistoricalData - Median Price.csv')
    # clean = clean_median(median)

    col = ["Mon-Yr", area]
    median_df = df[col].copy()

    median_df = median_df[median_df["Mon-Yr"].dt.month == 12].copy()

    median_df["Year"] = median_df["Mon-Yr"].dt.year
    median_df.drop("Mon-Yr", axis=1, inplace=True)

    return median_df


def get_unit_estimates(df, area):
    units_df = df[df["Area"] ==  area]
    units_df = units_df.melt(
        id_vars="Area",
        var_name="Year",
        value_name="units")

    units_df.drop("Area", axis=1, inplace=True)

    units_df["Year"] = units_df["Year"].astype(str).str.strip().astype(int)

    return units_df









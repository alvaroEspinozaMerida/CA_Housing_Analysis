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
        .replace({r'\$': '', ',': '', '--': '', '—': '','NA':'', 'N/A': '', 'null': ''}, regex=True)
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
        axis=0,
        ignore_index=True
    )

    cols = ['Mortgage', 'HE Revolving', 'Auto Loan', 'Credit Card',
       'Other', 'Total']

    debt_all[cols] = debt_all[cols].astype(float)

    return debt_all


def get_debt(df, category):
    df = df.drop('year', axis=1)
    col = [category, "quarter_start"]
    new_df = df[col].copy()
    new_df = new_df[new_df["quarter_start"].dt.month == 10].copy()
    new_df["year"] = new_df["quarter_start"].dt.year

    new_df.drop("quarter_start", axis=1, inplace=True)

    return new_df


def get_median_prices(df,area):
    #extract median prices for a specific area in format where year is a column
    # median = load_raw_data('MedianPricesofExistingDetachedHomesHistoricalData - Median Price.csv')
    # clean = clean_median(median)

    col = ["Mon-Yr", area]
    median_df = df[col].copy()

    median_df = median_df[median_df["Mon-Yr"].dt.month == 12].copy()

    median_df["year"] = median_df["Mon-Yr"].dt.year
    median_df.drop("Mon-Yr", axis=1, inplace=True)

    return median_df


def get_unit_estimates(df, area):
    units_df = df[df["Area"] ==  area]
    units_df = units_df.melt(
        id_vars="Area",
        var_name="year",
        value_name="units")

    units_df.drop("Area", axis=1, inplace=True)

    units_df["year"] = units_df["year"].astype(str).str.strip().astype(int)

    return units_df

#Combine all debt data into one dataframe; biggest issue with
# original is that debt_pre_2003 has to be transposed
def generate_all_debt():
    debt_df = load_raw_data('debt_2003_2025_clean.csv')

    debt_df2 = load_raw_data('debt_pre_2003.csv')
    debt_df2 = debt_df2.T

    debt_df2.columns = debt_df2.iloc[0]
    debt_df2 = debt_df2[1:]

    debt_df2 = debt_df2.reset_index()
    debt_df2 = debt_df2.rename(columns={"index": "quarter"})


    debt_all = pd.concat(
        [debt_df2, debt_df],
        axis=0,  # stack rows
        ignore_index=True
    )
    debt_all = debt_all.drop(debt_all.columns[0], axis=1)
    debt_all.to_csv('debt_all_years.csv')






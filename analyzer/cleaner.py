import pandas as pd


def clean_cdr(df):
    """
    Clean the uploaded CDR dataframe.
    """

    # Remove empty rows
    df = df.dropna(how="all")

    # Remove empty columns
    df = df.dropna(axis=1, how="all")

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    return df


def clean_ipdr(df):
    """
    Clean the uploaded IPDR dataframe.
    """

    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")
    df.columns = df.columns.str.strip()

    return df
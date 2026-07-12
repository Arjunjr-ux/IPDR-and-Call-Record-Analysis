import pandas as pd


def clean_ipdr_dataframe(df):
    """
    Cleans the IPDR dataframe before any report generation.
    """

    df = df.copy()

    # Clean column names
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    # Replace empty strings with NA
    df.replace("", pd.NA, inplace=True)

    return df
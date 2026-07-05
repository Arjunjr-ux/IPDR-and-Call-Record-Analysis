import pandas as pd

def validate_columns(df, required_columns):

    missing_columns = []

    for column in required_columns:
        if column not in df.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {', '.join(missing_columns)}"
        )

def clean_phone_number(value):

    if pd.isna(value):
        return ""

    value = str(value)

    value = "".join(ch for ch in value if ch.isdigit())

    if len(value) > 10:
        value = value[-10:]

    return value.strip()    

def clean_cdr(df):

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    # Remove spaces from column names
    df.columns = df.columns.map(str)
    df.columns = df.columns.str.strip()

    # Remove spaces from every string value
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].astype(str).str.strip()

    # Replace blank strings with NaN
    df.replace("", pd.NA, inplace=True)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Reset index
    df.reset_index(drop=True, inplace=True)
    
    required_columns = [
        "Target No",
        "Call Type",
        "Date",
        "Time"
    ]

    validate_columns(df, required_columns)
    
    phone_columns = [
        "Target No",
        "B Party No"
    ]

    for column in phone_columns:

        if column in df.columns:

            df[column] = df[column].apply(clean_phone_number)
    
    df = df[df["B Party No"].str.len() == 10]
    df = df[df["Target No"].str.len() == 10]
    
    if "Date" in df.columns:

        df["Date"] = pd.to_datetime(
            df["Date"],
            errors="coerce"
        )
        
        df = df.dropna(subset=["Date"])
        
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
    
    # Convert Time column
    if "Time" in df.columns:

        df["Time"] = pd.to_datetime(
            df["Time"],
            format="%H:%M:%S",
            errors="coerce"
        ).dt.time
    
    # Convert Duration column to numeric
    if "Dur(s)" in df.columns:

        df["Dur(s)"] = pd.to_numeric(
            df["Dur(s)"],
            errors="coerce"
        )

        df["Dur(s)"] = df["Dur(s)"].fillna(0)
    
    return df


def clean_ipdr(df):

    df = df.dropna(how="all")

    df = df.dropna(axis=1, how="all")

    df.columns = df.columns.map(str)
    df.columns = df.columns.str.strip()

    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].astype(str).str.strip()

    df.replace("", pd.NA, inplace=True)

    df = df.drop_duplicates()

    df = df.reset_index(drop=True)

    required_columns = [
        "Source IP Address",
        "Destination IP Address",
        "Start Date of Public IP Allocation"
    ]

    validate_columns(df, required_columns)
    
    phone_columns = [
        "MSISDN"
    ]

    for column in phone_columns:

        if column in df.columns:

            df[column] = df[column].apply(clean_phone_number)
    
    date_columns = [
    "Start Date of Public IP Allocation",
    "End Date of Public IP Allocation"
    ]

    for column in date_columns:

        if column in df.columns:

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )
            
            df = df.dropna(subset=[column])
            
            df[column] = df[column].dt.strftime("%Y-%m-%d")

    time_columns = [
    "Start Time",
    "End Time",
    "Time"
    ]

    for column in time_columns:

        if column in df.columns:

            df[column] = pd.to_datetime(
                df[column],
                format="%H:%M:%S",
                errors="coerce"
            ).dt.time    
    
    numeric_columns = [
    "Session Duration"
    ]

    for column in numeric_columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

            df[column] = df[column].fillna(0)
    
    return df
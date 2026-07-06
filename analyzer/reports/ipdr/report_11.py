def generate(df):
    """
    Report 11: IMSI Summary
    """

    return {
        "Unique IMSI": df["IMSI"].nunique()
    }
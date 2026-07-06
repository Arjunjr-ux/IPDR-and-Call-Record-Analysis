def generate(df):
    """
    Report 12: Device Summary
    """

    devices = (
        df["Device Identification number"]
        .astype(str)
        .value_counts()
        .head(10)
    )

    return devices
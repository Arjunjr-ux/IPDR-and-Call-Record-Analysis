def generate(df):
    """
    Report 03: Top 10 Source IP Addresses
    """

    top_source_ips = df["Source IP Address"].value_counts().head(10)

    return top_source_ips
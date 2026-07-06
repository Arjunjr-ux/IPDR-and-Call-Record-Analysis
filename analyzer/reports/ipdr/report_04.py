def generate(df):
    """
    Report 04: Top 10 Destination IP Addresses
    """

    top_destination_ips = df["Destination IP Address"].value_counts().head(10)

    return top_destination_ips
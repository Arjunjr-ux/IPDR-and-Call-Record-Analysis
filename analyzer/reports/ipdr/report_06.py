def generate(df):
    """
    Report 06: Top Destination Ports
    """

    top_ports = df["Destination Port"].value_counts().head(10)

    return top_ports
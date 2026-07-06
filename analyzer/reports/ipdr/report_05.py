def generate(df):
    """
    Report 05: Top Source Ports
    """

    top_ports = df["Source Port"].value_counts().head(10)

    return top_ports
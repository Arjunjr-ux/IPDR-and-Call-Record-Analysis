def generate(df):
    """
    Report 07: Public IP Summary
    """

    return {
        "Total Public IP Records": len(df),
        "Unique Public IPs": df["Public IP Address"].nunique()
    }
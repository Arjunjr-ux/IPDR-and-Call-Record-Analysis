def generate(df):
    """
    Report 13: Roaming Summary
    """

    return {
        "Roaming Indicator": df["Roaming Circle Indicator"].value_counts(),
        "Roaming Circle": df["Roaming Circle"].value_counts()
    }
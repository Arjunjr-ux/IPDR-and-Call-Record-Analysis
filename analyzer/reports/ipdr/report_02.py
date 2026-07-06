def generate(df):
    """
    Report 02: Unique Internet Subscribers
    """

    unique_subscribers = df["Landline/MSISDN for Internet Access"].nunique()

    return {
        "Report Name": "Unique Internet Subscribers",
        "Unique Subscribers": unique_subscribers
    }
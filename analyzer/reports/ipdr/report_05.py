def generate(df):
    """
    Official Report 05
    Per-Subscriber Activity & Top-Talker Profiling
    """

    report = (
        df.groupby("Landline/MSISDN for Internet Access")
        .agg(
            Session_Count=("Landline/MSISDN for Internet Access", "count"),
            Distinct_Destination_IPs=("Destination IP Address", "nunique"),
            Total_Session_Duration=("Session Duration", "sum"),
            Average_Session_Duration=("Session Duration", "mean"),
            Port_Spread=("Destination Port", "nunique"),
        )
        .sort_values(by="Session_Count", ascending=False)
        .reset_index()
    )

    return report
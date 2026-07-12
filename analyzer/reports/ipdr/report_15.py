import pandas as pd


def generate(df):
    """
    Official Report 15
    Temporal Traffic Pattern, Burst & NAT Allocation Analysis
    """

    report = df[
        [
            "Time1",
            "Landline/MSISDN for Internet Access",
            "Public IP Address",
        ]
    ].copy()

    report = report.rename(
        columns={
            "Time1": "Activity Time",
            "Landline/MSISDN for Internet Access": "Subscriber",
            "Public IP Address": "Public IP",
        }
    )

    # Convert to datetime
    report["Activity Time"] = pd.to_datetime(
        report["Activity Time"],
        dayfirst=True,
        errors="coerce",
    )

    # Remove invalid timestamps
    report = report.dropna(subset=["Activity Time"])

    # Count sessions per timestamp
    timeline = (
        report.groupby("Activity Time")
        .agg(
            Total_Sessions=("Subscriber", "count"),
            Unique_Subscribers=("Subscriber", "nunique"),
            Public_IPs=("Public IP", "nunique"),
        )
        .reset_index()
    )

    timeline = timeline.sort_values(
        by="Activity Time",
        ignore_index=True,
    )

    return timeline
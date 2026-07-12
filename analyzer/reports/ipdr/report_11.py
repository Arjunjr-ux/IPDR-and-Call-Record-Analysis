import pandas as pd


def generate(df):
    """
    Official Report 11
    High-Duration / Bulk-Transfer Session Outliers
    """

    report = df[
        [
            "Landline/MSISDN for Internet Access",
            "Destination IP Address",
            "Destination Port",
            "Time1",
            "Session Duration",
        ]
    ].copy()

    report = report.rename(
        columns={
            "Landline/MSISDN for Internet Access": "Subscriber",
            "Destination IP Address": "Destination IP",
            "Destination Port": "Port",
            "Time1": "Session Time",
        }
    )

    report = report.sort_values(
        by="Session Duration",
        ascending=False,
        ignore_index=True,
    )

    return report
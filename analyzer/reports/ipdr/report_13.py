import pandas as pd


def generate(df):
    """
    Official Report 13
    Roaming, Circle & Cell Location (CGI) Analysis
    """

    report = df[
        [
            "Landline/MSISDN for Internet Access",
            "Time1",
            "Roaming Circle Indicator",
            "Roaming Circle",
            "CGI ID",
        ]
    ].copy()

    report = report.rename(
        columns={
            "Landline/MSISDN for Internet Access": "Subscriber",
            "Time1": "Activity Time",
            "Roaming Circle Indicator": "Roaming Status",
            "Roaming Circle": "Circle",
            "CGI ID": "CGI",
        }
    )

    report = report.sort_values(
        by=["Subscriber", "Activity Time"],
        ignore_index=True,
    )

    return report
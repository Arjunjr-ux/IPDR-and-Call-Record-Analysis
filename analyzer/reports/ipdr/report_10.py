import pandas as pd


def generate(df):
    """
    Official Report 10
    Session Timeline & Online Presence Reconstruction
    """

    report = df[
        [
            "Landline/MSISDN for Internet Access",
            "Public IP Address",
            "Start Date of Public IP Allocation",
            "IST Start Time of Public IP Allocation",
            "End Date of Public IP Allocation",
            "IST End Time of Public IP Allocation",
            "Time1",
            "Session Duration",
        ]
    ].copy()

    report["Session Start"] = (
        report["Start Date of Public IP Allocation"].astype(str)
        + " "
        + report["IST Start Time of Public IP Allocation"].astype(str)
    )

    report["Session End"] = (
        report["End Date of Public IP Allocation"].astype(str)
        + " "
        + report["IST End Time of Public IP Allocation"].astype(str)
    )

    report = report.rename(
        columns={
            "Landline/MSISDN for Internet Access": "Subscriber",
            "Public IP Address": "Public IP",
            "Time1": "Activity Time",
        }
    )

    report = report[
        [
            "Subscriber",
            "Public IP",
            "Session Start",
            "Session End",
            "Activity Time",
            "Session Duration",
        ]
    ]

    report = report.sort_values(
        by=["Subscriber", "Activity Time"],
        ignore_index=True,
    )

    return report
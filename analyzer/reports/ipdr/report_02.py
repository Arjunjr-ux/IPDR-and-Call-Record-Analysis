import pandas as pd


def generate(df):
    """
    Report 02
    Reverse Destination Lookup
    """

    report = df[
        [
            "Landline/MSISDN for Internet Access",
            "Destination IP Address",
            "Destination Port",
            "Public IP Address",
            "IMSI",
            "Device Identification number",
            "Time1",
        ]
    ].copy()

    report = report.rename(
        columns={
            "Landline/MSISDN for Internet Access": "Subscriber",
            "Destination IP Address": "Destination IP",
            "Destination Port": "Destination Port",
            "Public IP Address": "Public IP",
            "Device Identification number": "IMEI",
            "Time1": "Session Time",
        }
    )

    report = report.sort_values(
        by=["Destination IP", "Session Time"],
        ignore_index=True,
    )

    return report
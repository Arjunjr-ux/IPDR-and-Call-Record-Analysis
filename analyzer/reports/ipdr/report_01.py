import pandas as pd


def generate(df):
    """
    Report 01
    CGNAT Public IP -> Subscriber Resolution
    """

    report = df[
        [
            "Landline/MSISDN for Internet Access",
            "Public IP Address",
            "Public IP Port",
            "Source Port",
            "Start Date of Public IP Allocation",
            "IST Start Time of Public IP Allocation",
            "End Date of Public IP Allocation",
            "IST End Time of Public IP Allocation",
            "IMSI",
            "Device Identification number",
        ]
    ].copy()

    report = report.rename(
        columns={
            "Landline/MSISDN for Internet Access": "Subscriber",
            "Public IP Address": "Public IP",
            "Public IP Port": "Public Port",
            "Source Port": "Source Port",
            "Start Date of Public IP Allocation": "Start Date",
            "IST Start Time of Public IP Allocation": "Start Time",
            "End Date of Public IP Allocation": "End Date",
            "IST End Time of Public IP Allocation": "End Time",
            "Device Identification number": "IMEI",
        }
    )

    report = report.drop_duplicates()

    report = report.sort_values(
        by=["Start Date", "Start Time"],
        ignore_index=True,
    )

    return report
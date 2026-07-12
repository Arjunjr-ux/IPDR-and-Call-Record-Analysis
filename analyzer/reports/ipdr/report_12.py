import pandas as pd


def generate(df):
    """
    Official Report 12
    Device & SIM Fingerprinting & Integrity Analysis
    """

    report = df[
        [
            "Landline/MSISDN for Internet Access",
            "Device Identification number",
            "IMSI",
        ]
    ].copy()

    report = report.rename(
        columns={
            "Landline/MSISDN for Internet Access": "MSISDN",
            "Device Identification number": "IMEI",
            "IMSI": "IMSI",
        }
    )
    # Remove rows with missing identifiers
    report = report.dropna(subset=["MSISDN", "IMEI", "IMSI"])

    # Remove duplicate combinations
    report = report.drop_duplicates()

    # Count relationships
    imei_count = report.groupby("IMEI")["IMSI"].nunique()
    imsi_count = report.groupby("IMSI")["IMEI"].nunique()
    msisdn_count = report.groupby("IMEI")["MSISDN"].nunique()

    status = []

    for _, row in report.iterrows():

        flags = []

        if imei_count[row["IMEI"]] > 1:
            flags.append("Multiple IMSIs")

        if imsi_count[row["IMSI"]] > 1:
            flags.append("Multiple IMEIs")

        if msisdn_count[row["IMEI"]] > 1:
            flags.append("Multiple MSISDNs")

        if not flags:
            flags.append("Normal")

        status.append(", ".join(flags))

    report["Integrity Status"] = status

    return report.sort_values(
        by=["MSISDN"],
        ignore_index=True,
    )
import pandas as pd


def generate(df):
    """
    Official Report 14
    Common-Destination Co-occurrence & Link Analysis
    """

    # Keep only required columns
    report = df[
        [
            "Landline/MSISDN for Internet Access",
            "Destination IP Address",
        ]
    ].copy()

    report = report.rename(
        columns={
            "Landline/MSISDN for Internet Access": "Subscriber",
            "Destination IP Address": "Destination IP",
        }
    )

    # Remove duplicate Subscriber -> Destination pairs
    report = report.drop_duplicates()

    # Count unique subscribers per destination
    grouped = (
        report.groupby("Destination IP")
        .agg(
            Subscribers=("Subscriber", "nunique"),
            Subscriber_List=("Subscriber", lambda x: ", ".join(sorted(set(map(str, x)))))
        )
        .reset_index()
    )

    # Keep only IPs used by more than one subscriber
    grouped = grouped[grouped["Subscribers"] > 1]

    # Remove common infrastructure (can be expanded later)
    common_ips = [
        "208.67.222.222",   # OpenDNS
    ]

    grouped = grouped[
        ~grouped["Destination IP"].isin(common_ips)
    ]

    # Sort by number of subscribers
    grouped = grouped.sort_values(
        by="Subscribers",
        ascending=False,
        ignore_index=True,
    )

    return grouped
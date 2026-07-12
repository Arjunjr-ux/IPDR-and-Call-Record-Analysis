import pandas as pd


def classify_service(row):
    port = row["Destination Port"]
    ip = str(row["Destination IP Address"])

    try:
        port = int(port)
    except:
        return None

    # OpenDNS
    if ip == "208.67.222.222":
        return "OpenDNS"

    # DNS
    if port == 53:
        return "DNS"

    # DNS over TLS
    if port == 853:
        return "DNS-over-TLS"

    # NTP
    if port == 123:
        return "NTP"

    return None


def generate(df):
    """
    Official Report 09
    DNS & NTP Infrastructure Behaviour Profiling
    """

    report = df.copy()

    report["Service"] = report.apply(classify_service, axis=1)

    report = report[report["Service"].notna()]

    summary = (
        report.groupby(
            [
                "Landline/MSISDN for Internet Access",
                "Service",
            ]
        )
        .size()
        .reset_index(name="Sessions")
    )

    summary = summary.rename(
        columns={
            "Landline/MSISDN for Internet Access": "Subscriber"
        }
    )

    summary = summary.sort_values(
        by=["Service", "Sessions"],
        ascending=[True, False],
    )

    return summary
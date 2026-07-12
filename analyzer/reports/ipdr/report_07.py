def classify_risk(port):
    try:
        port = int(port)
    except:
        return None

    risk_ports = {
        6881: "BitTorrent / P2P",
        5222: "Encrypted Chat (XMPP)",
        4222: "Messaging Protocol (4222)",
        8080: "Proxy / Alternate HTTP",
        8888: "Proxy / Alternate HTTP",
        853: "Encrypted DNS (DoT)",
        0: "Malformed / Uncommon Port",
    }

    return risk_ports.get(port)


def generate(df):
    """
    Official Report 07
    Suspicious / High-Risk Protocol & Anomalous-Port Detection
    """

    report = df.copy()

    report["Risk Category"] = report["Destination Port"].apply(classify_risk)

    report = report[report["Risk Category"].notna()]

    summary = (
        report.groupby(
            [
                "Risk Category",
                "Landline/MSISDN for Internet Access",
            ]
        )
        .size()
        .reset_index(name="Suspicious Sessions")
    )

    summary = summary.sort_values(
        by=[
            "Risk Category",
            "Suspicious Sessions",
        ],
        ascending=[True, False],
    )

    summary = summary.rename(
        columns={
            "Landline/MSISDN for Internet Access": "Subscriber"
        }
    )

    return summary
import pandas as pd

from analyzer.services.ip_service import lookup_ip


def generate(df):
    """
    Report 08

    VPN / Proxy / Tor / Anonymiser Detection
    """

    required_columns = [
        "Landline/MSISDN for Internet Access",
        "Destination IP Address",
        "Destination Port",
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(
                f"Missing required column: {column}"
            )

    print("Detecting VPN / Proxy / Tor usage...")

    suspicious_ports = {
        8080,
        8888,
        4222,
        3128,
        1080,
        853,
        6881,
    }

    cache = {}

    records = []

    for _, row in df.iterrows():

        ip = row["Destination IP Address"]

        if ip not in cache:
            cache[ip] = lookup_ip(ip)

        info = cache[ip]

        try:
            port = int(row["Destination Port"])
        except Exception:
            port = 0

        proxy_port = "Yes" if port in suspicious_ports else "No"

        risk_score = 0

        if info["vpn"] == "Yes":
            risk_score += 1

        if info["proxy"] == "Yes":
            risk_score += 1

        if info["tor"] == "Yes":
            risk_score += 1

        if proxy_port == "Yes":
            risk_score += 1

        records.append(
            {
                "MSISDN": row["Landline/MSISDN for Internet Access"],
                "Destination IP": ip,
                "Destination Port": port,
                "Organization": info["organization"],
                "ASN": info["asn"],
                "Hosting": info["hosting"],
                "Country": info["country"],
                "VPN": info["vpn"],
                "Proxy": info["proxy"],
                "Tor": info["tor"],
                "Proxy Port": proxy_port,
                "Risk Score": risk_score,
            }
        )

    report = pd.DataFrame(records)

    report = report.sort_values(
        by="Risk Score",
        ascending=False,
    )

    return report.reset_index(drop=True)
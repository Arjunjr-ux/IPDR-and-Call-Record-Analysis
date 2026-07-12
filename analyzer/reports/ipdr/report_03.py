import pandas as pd

from analyzer.services.ip_service import lookup_ip


def generate(df):
    """
    Report 03

    Destination IP & Service Attribution
    """

    print("Looking up destination IP intelligence...")

    report = (
        df.groupby("Destination IP Address")
        .size()
        .reset_index(name="Session Count")
        .sort_values(
            by="Session Count",
            ascending=False
        )
        .reset_index(drop=True)
    )

    organizations = []
    asns = []
    countries = []
    hostings = []
    services = []

    cache = {}

    for ip in report["Destination IP Address"]:

        if ip not in cache:
            cache[ip] = lookup_ip(ip)

        info = cache[ip]

        organizations.append(info["organization"])
        asns.append(info["asn"])
        countries.append(info["country"])
        hostings.append(info["hosting"])

        service = info["service"]

        if service == "Unknown":

            if info["organization"] != "Unknown":
                service = info["organization"]

            elif info["hosting"] != "Unknown":
                service = info["hosting"]

            else:
                service = "General Internet"

        services.append(service)

    report["Organization"] = organizations
    report["ASN"] = asns
    report["Country"] = countries
    report["Hosting"] = hostings
    report["Service Category"] = services

    report = report[
        [
            "Destination IP Address",
            "Organization",
            "ASN",
            "Service Category",
            "Hosting",
            "Country",
            "Session Count",
        ]
    ]

    return report
import pandas as pd

from analyzer.services.ip_service import lookup_ip


def generate(df):
    """
    Report 04

    Destination Geolocation &
    Foreign Communication Mapping

    Maps every destination IP to its
    country, region and city and
    classifies communications as
    Domestic or Foreign.
    """

    required_columns = [
        "Destination IP Address",
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(
                f"Missing required column: {column}"
            )

    print("Mapping destination geolocation...")

    report = (
        df.groupby("Destination IP Address")
        .size()
        .reset_index(name="Session Count")
        .sort_values(
            by="Session Count",
            ascending=False,
        )
        .reset_index(drop=True)
    )

    countries = []
    regions = []
    cities = []
    communication = []

    cache = {}

    for ip in report["Destination IP Address"]:

        if ip not in cache:
            cache[ip] = lookup_ip(ip)

        info = cache[ip]

        country = info["country"]
        region = info["region"]
        city = info["city"]

        countries.append(country)
        regions.append(region)
        cities.append(city)

        if country.lower() == "india":
            communication.append("Domestic")

        elif country == "Unknown":
            communication.append("Unknown")

        else:
            communication.append("Foreign")

    report["Country"] = countries
    report["Region"] = regions
    report["City"] = cities
    report["Communication Type"] = communication

    return report[
        [
            "Destination IP Address",
            "Country",
            "Region",
            "City",
            "Communication Type",
            "Session Count",
        ]
    ]
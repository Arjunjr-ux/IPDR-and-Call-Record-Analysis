import os
import pandas as pd
import IP2Location


# -----------------------------
# Load IP2Location BIN database
# -----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BIN_DATABASE = os.path.join(
    BASE_DIR,
    "databases",
    "IP2LOCATION-LITE-DB11.BIN",
)

CSV_DATABASE = os.path.join(
    BASE_DIR,
    "data",
    "ip_intelligence.csv",
)

ip2location_db = IP2Location.IP2Location()

if os.path.exists(BIN_DATABASE):
    ip2location_db.open(BIN_DATABASE)

# -----------------------------
# Load Intelligence Database
# -----------------------------

if os.path.exists(CSV_DATABASE):
    intelligence_db = pd.read_csv(CSV_DATABASE)
else:
    intelligence_db = pd.DataFrame()


# -----------------------------
# Search Intelligence CSV
# -----------------------------

def search_intelligence(ip):

    if intelligence_db.empty:
        return None

    row = intelligence_db[
        intelligence_db["IP Address"] == ip
    ]

    if row.empty:
        return None

    row = row.iloc[0]

    return {
        "organization": row.get("Organization", "Unknown"),
        "asn": row.get("ASN", "Unknown"),
        "service": row.get("Service", "Unknown"),
        "hosting": row.get("Hosting", "Unknown"),
        "vpn": row.get("VPN", "Unknown"),
        "proxy": row.get("Proxy", "Unknown"),
        "tor": row.get("Tor", "Unknown"),
    }


# -----------------------------
# Offline Lookup
# -----------------------------

def lookup_ip(ip):

    result = {
        "ip": ip,
        "country": "Unknown",
        "region": "Unknown",
        "city": "Unknown",
        "isp": "Unknown",
        "organization": "Unknown",
        "asn": "Unknown",
        "service": "Unknown",
        "hosting": "Unknown",
        "vpn": "Unknown",
        "proxy": "Unknown",
        "tor": "Unknown",
    }

    # ---------- IP2Location ----------

    try:

        record = ip2location_db.get_all(ip)

        if record:

            result["country"] = getattr(
                record,
                "country_long",
                "Unknown",
            )

            result["region"] = getattr(
                record,
                "region",
                "Unknown",
            )

            result["city"] = getattr(
                record,
                "city",
                "Unknown",
            )

            result["isp"] = getattr(
                record,
                "isp",
                "Unknown",
            )

    except Exception:
        pass

    # ---------- Intelligence CSV ----------

    intel = search_intelligence(ip)

    if intel:

        result["organization"] = intel["organization"]
        result["asn"] = intel["asn"]
        result["service"] = intel["service"]
        result["hosting"] = intel["hosting"]
        result["vpn"] = intel["vpn"]
        result["proxy"] = intel["proxy"]
        result["tor"] = intel["tor"]

    return result
def generate(df):
    """
    Report 15: Overall IPDR Summary
    """

    # Safely get the most common APN
    apn_mode = df["Access Point Name"].mode()

    if len(apn_mode) > 0:
        top_apn = apn_mode.iloc[0]
    else:
        top_apn = "No APN Data"

    return {
        "Total Records": len(df),
        "Unique Subscribers": df["Landline/MSISDN for Internet Access"].nunique(),
        "Unique IMSI": df["IMSI"].nunique(),
        "Unique Public IP": df["Public IP Address"].nunique(),
        "Top APN": top_apn,
        "Average Session Duration": df["Session Duration"].mean()
    }
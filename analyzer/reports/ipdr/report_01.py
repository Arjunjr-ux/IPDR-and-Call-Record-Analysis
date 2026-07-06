def generate(df):
    """
    Report 01: Total IPDR Records
    """

    total_records = len(df)

    return {
        "Report Name": "Total IPDR Records",
        "Total Records": total_records
    }
import pandas as pd


def generate(df):

    report = {}

    report["report_name"] = "Top Associate Report"

    total_calls = (
        df.groupby("B Party No")
        .size()
        .sort_values(ascending=False)
    )

    report["top_contacts"] = total_calls.head(10)

    return report
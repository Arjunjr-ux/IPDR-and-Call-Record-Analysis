import pandas as pd


def generate(df):

    report = {}

    report["report_name"] = "Top Associate Report"
    
    print(df["B Party No"].unique())
    
    print(df["B Party No"].value_counts(dropna=False))
    
    total_calls = (
        df.groupby("B Party No")
        .size()
        .sort_values(ascending=False)
    )

    report["top_contacts"] = total_calls.head(10).to_dict()

    return report
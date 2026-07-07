import os
import pandas as pd

from analyzer.utils import clean_ipdr_dataframe
from analyzer.ipdr_reports import generate_all_reports

df = pd.read_excel(
    "analyzer/test_data/IPDR Practical.xlsx",
    header=8,
)

df = clean_ipdr_dataframe(df)

reports = generate_all_reports(df)

os.makedirs("output", exist_ok=True)

for name, report in reports.items():
    report.to_csv(f"output/{name}.csv", index=False)

print("Report 01 generated successfully!")
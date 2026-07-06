import pandas as pd

from analyzer.ipdr_reports import generate_all_reports

df = pd.read_excel(
    "analyzer/test_data/IPDR Practical.xlsx",
    header=8
)

reports = generate_all_reports(df)

for name, report in reports.items():
    print(f"\n{name}")
    print(report)

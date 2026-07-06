import os
import pandas as pd

from analyzer.ipdr_reports import generate_all_reports

# Read the IPDR file
df = pd.read_excel("analyzer/test_data/IPDR Practical.xlsx", header=8)

# Generate all reports
reports = generate_all_reports(df)

# Create output folder
os.makedirs("output", exist_ok=True)

# Save each report
for name, report in reports.items():

    if isinstance(report, pd.Series):
        report.to_csv(f"output/{name}.csv")

    elif isinstance(report, dict):
        pd.DataFrame([report]).to_csv(f"output/{name}.csv", index=False)

print("All reports saved successfully!")

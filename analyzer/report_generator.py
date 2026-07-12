from analyzer.reports.cdr.report_01 import generate as cdr_report_01
from analyzer.reports.ipdr.report_01 import generate as ipdr_report_01
from analyzer.reports.combined.report_01 import generate as combined_report_01


def generate_all_reports(cdr_df, ipdr_df):
    
    results = {
    "cdr": None,
    "ipdr": None,
    "combined": None
    }

    results["cdr"] = cdr_report_01(cdr_df)
    results["ipdr"] = ipdr_report_01(ipdr_df)
    results["combined"] = combined_report_01(cdr_df, ipdr_df)

    return results
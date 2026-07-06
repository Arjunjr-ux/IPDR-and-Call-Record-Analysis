from .reports.ipdr import report_01
def generate_ipdr_reports(ipdr_df):

    reports = {}

    reports["report_01"] = report_01.generate(ipdr_df)

    return reports
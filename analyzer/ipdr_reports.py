from analyzer.reports.ipdr import report_01


def generate_all_reports(df):

    return {
        "report_01": report_01.generate(df),
    }
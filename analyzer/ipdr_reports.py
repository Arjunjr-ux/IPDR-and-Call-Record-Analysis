from analyzer.reports.ipdr import report_01, report_02,report_05


def generate_all_reports(df):

    return {
        "report_01": report_01.generate(df),
        "report_02": report_02.generate(df),
        "report_05": report_05.generate(df),
    }
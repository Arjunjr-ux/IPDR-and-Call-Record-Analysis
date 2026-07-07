from analyzer.reports.ipdr import report_01, report_02,report_05, report_06, report_07, report_09, report_10, report_11, report_13, report_14, report_15


def generate_all_reports(df):

    return {
        "report_01": report_01.generate(df),
        "report_02": report_02.generate(df),
        "report_05": report_05.generate(df),
        "report_06": report_06.generate(df),
        "report_07": report_07.generate(df),
        "report_09": report_09.generate(df),
        "report_10": report_10.generate(df),
        "report_11": report_11.generate(df),
        "report_13": report_13.generate(df),
        "report_14": report_14.generate(df),
        "report_15": report_15.generate(df),
    }
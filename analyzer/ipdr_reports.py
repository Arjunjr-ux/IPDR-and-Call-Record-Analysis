from .reports.ipdr import report_01
from .reports.ipdr import report_02
from .reports.ipdr import report_03
from .reports.ipdr import report_04
from .reports.ipdr import report_05
from .reports.ipdr import report_06
from .reports.ipdr import report_07
from .reports.ipdr import report_08
from .reports.ipdr import report_09
from .reports.ipdr import report_10
from .reports.ipdr import report_11
from .reports.ipdr import report_12
from .reports.ipdr import report_13
from .reports.ipdr import report_14
from .reports.ipdr import report_15


def generate_all_reports(df):
    return {
        "report_01": report_01.generate(df),
        "report_02": report_02.generate(df),
        "report_03": report_03.generate(df),
        "report_04": report_04.generate(df),
        "report_05": report_05.generate(df),
        "report_06": report_06.generate(df),
        "report_07": report_07.generate(df),
        "report_08": report_08.generate(df),
        "report_09": report_09.generate(df),
        "report_10": report_10.generate(df),
        "report_11": report_11.generate(df),
        "report_12": report_12.generate(df),
        "report_13": report_13.generate(df),
        "report_14": report_14.generate(df),
        "report_15": report_15.generate(df),
    }
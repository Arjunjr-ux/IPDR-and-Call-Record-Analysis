import pandas as pd

from django.shortcuts import render

from .report_generator import generate_all_reports
from .cleaner import clean_cdr, clean_ipdr


def home(request):

    if request.method == "POST":

        cdr_file = request.FILES.get("cdr_file")
        ipdr_file = request.FILES.get("ipdr_file")

        cdr_df = clean_cdr(
            pd.read_excel(cdr_file, header=6)
        )
        
        ipdr_df = clean_ipdr(
            pd.read_excel(ipdr_file, header=8)
        )

        try:

            results = generate_all_reports(
                cdr_df,
                ipdr_df
            )

            return render(
                request,
                "home.html",
                {
                    "cdr_results": results["cdr"][0],
                    "ipdr_results": results["ipdr"][0],
                    "combined_results": results["combined"][0],
                }
            )

        except Exception as e:

            return render(
                request,
                "home.html",
                {
                    "error": str(e)
                }
            )
        

    return render(request, "home.html")
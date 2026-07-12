import pandas as pd

from django.shortcuts import render

from .report_generator import generate_all_reports
from .cleaner import clean_cdr, clean_ipdr


def home(request):

    dashboard = request.session.get("dashboard", {})

    return render(

        request,

        "dashboard/dashboard.html",

        dashboard

    )


def dashboard(request):

    return render(
        request,
        "dashboard/dashboard.html"
    )

def risk(request):
    return render(
        request,
        "risk/risk.html"
    )

def tables(request):

    return render(
        request,
        "tables/tables.html"
    )

def upload(request):

    if request.method == "POST":

        cdr_file = request.FILES.get("cdr_file")
        ipdr_file = request.FILES.get("ipdr_file")

        try:

            cdr_df = clean_cdr(
                pd.read_excel(cdr_file, header=6)
            )

            ipdr_df = clean_ipdr(
                pd.read_excel(ipdr_file, header=8)
            )

            results = generate_all_reports(
                cdr_df,
                ipdr_df
            )

            request.session["cdr_results"] = results["cdr"]
            
            print("Saved to session:")
            print(request.session["cdr_results"])
            
            request.session["ipdr_results"] = results["ipdr"]
            request.session["combined_results"] = results["combined"]
            
            request.session["dashboard"] = {

                "cdr_count": len(cdr_df),

                "ipdr_count": len(ipdr_df),

                "report_count":
                    len(results["cdr"])
                    + len(results["ipdr"])
                    + len(results["combined"]),

                "total_files": 2

            }
            
            return render(
                request,
                "report/report.html",
                {
                    "cdr_results": results["cdr"],
                    "ipdr_results": results["ipdr"],
                    "combined_results": results["combined"],

                    "cdr_count": len(cdr_df),
                    "ipdr_count": len(ipdr_df),
                    "report_count": (
                        len(results["cdr"]) +
                        len(results["ipdr"]) +
                        len(results["combined"])
                    )
                }
            )

        except Exception as e:

            return render(
                request,
                "upload/upload.html",
                {
                    "error": str(e)
                }
            )

    return render(
        request,
        "upload/upload.html"
    )


def reports(request):

    return render(
        request,
        "report/report.html"
    )    


def cdr_report(request):

    print("Session data:")
    print(request.session.get("cdr_results"))

    return render(
        request,
        "view_reports/cdr.html",
        {
            "cdr_results": request.session.get("cdr_results")
        }
    )


def ipdr_report(request):

    return render(
        request,
        "view_reports/ipdr.html"
    )


def combined_report(request):

    return render(
        request,
        "view_reports/combined.html"
    )
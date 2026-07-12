"""
URL configuration for telecom_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from analyzer import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="dashboard"),

    path("upload/", views.upload, name="upload"),

    path("reports/", views.reports, name="reports"),
    
    path("reports/cdr/", views.cdr_report, name="cdr_report"),
    
    path("reports/ipdr/", views.ipdr_report, name="ipdr_report"),
    
    path("reports/combined/", views.combined_report, name="combined_report"),

    path("risk/", views.risk, name="risk"),

    path("tables/", views.tables, name="tables"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path

from core.reports.views import ReportDiarioView, ReportPlancuentaView

urlpatterns = [
    # reports
    path('diario/', ReportDiarioView.as_view(), name='diario_report'),
    path('plancuenta/', ReportPlancuentaView.as_view(), name='plancuenta_report'),
]
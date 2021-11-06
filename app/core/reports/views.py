import os
from io import BytesIO
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from core.erp.models import Diario, Plancontable, Ingreso
from core.reports.forms import ReportForm

from django.db.models.functions import Coalesce
from django.db.models import Sum


class ReportIngresoView(TemplateView):
    template_name = 'ingreso/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Ingreso.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.cli.name,
                        s.date_joined.strftime('%Y-%m-%d'),
                        format(s.subtotal, '.2f'),
                        format(s.igv, '.2f'),
                        format(s.total, '.2f'),
                    ])

                subtotal = search.aggregate(r=Coalesce(Sum('subtotal'), 0)).get('r')
                igv = search.aggregate(r=Coalesce(Sum('igv'), 0)).get('r')
                total = search.aggregate(r=Coalesce(Sum('total'), 0)).get('r')

                data.append([
                    '---',
                    '---',
                    '---',
                    format(subtotal, '.2f'),
                    format(igv, '.2f'),
                    format(total, '.2f'),
                ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Ventas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('ingreso_report')
        context['form'] = ReportForm()
        return context


class ReportDiarioView(TemplateView):
    template_name = 'diario/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Diario.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.nro,
                        s.date_joined.strftime('%Y-%m-%d'),
                        s.cuenta.name,
                        s.desc,
                        format(s.debe, '.2f'),
                        format(s.haber, '.2f'),
                    ])

                debe = search.aggregate(r=Coalesce(Sum('debe'), 0)).get('r')
                haber = search.aggregate(r=Coalesce(Sum('haber'), 0)).get('r')
                # total = search.aggregate(r=Coalesce(Sum('total'), 0)).get('r')

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    format(debe, '.2f'),
                    format(haber, '.2f'),
                ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Diario Ingreso'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('diario_report')
        context['form'] = ReportForm()
        return context


class ReportPlancuentaView(TemplateView):
    template_name = 'plancuenta/report.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Plancontable.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(date_joined__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.date_joined,
                        s.tipo.name,
                        s.name,
                        format(s.total, '.2f'),
                    ])
                total = search.aggregate(r=Coalesce(Sum('total'), 0)).get('r')

                data.append([
                    '---',
                    '---',
                    '---',
                    '---',
                    format(total, '.2f'),
                ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte Plan contable'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('plancuenta_report')
        context['form'] = ReportForm()
        return context


# def index(request):
#     return HttpResponse("Hello")
#
# def report(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=Platzi-student-report.pdf'
#
#     buffer = BytesIO()
#     c = canvas.Canvas(buffer, pagesize=A4)
#
#     c.setLineWidth(.3)
#     c.setFont('Helvetica', 22)
#     c.drawString(30,750, 'Platzi')
#     c.setFont('Helvetica',12)
#     c.drawString(30,175, 'Report')
#
#
#     c.save()
#
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response
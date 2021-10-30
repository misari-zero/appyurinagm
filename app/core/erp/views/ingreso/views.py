import json
import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponse
from django.http import JsonResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from xhtml2pdf import pisa

from core.erp.forms import IngresoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Ingreso, Project, DetIngreso


class IngresoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Ingreso
    template_name = 'ingreso/list.html'
    permission_required = 'erp.view_ingreso'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Ingreso.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in DetIngreso.objects.filter(sale_id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ingresos'
        context['create_url'] = reverse_lazy('erp:ingreso_create')
        context['list_url'] = reverse_lazy('erp:ingreso_list')
        context['entity'] = 'Ingresos'
        return context


class IngresoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Ingreso
    form_class = IngresoForm
    template_name = 'ingreso/create.html'
    success_url = reverse_lazy('erp:ingreso_list')
    permission_required = 'erp.add_ingreso'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Project.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    # item['value'] = i.name
                    item['text'] = i.name
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    ingreso = Ingreso()
                    ingreso.doc = vents['doc']
                    ingreso.date_joined = vents['date_joined']
                    ingreso.date_venc = vents['date_venc']
                    ingreso.cli_id = vents['cli']
                    ingreso.subtotal = float(vents['subtotal'])
                    ingreso.igv = float(vents['igv'])
                    ingreso.total = float(vents['total'])
                    ingreso.save()
                    for i in vents['products']:
                        det = DetIngreso()
                        det.ingreso_id = ingreso.id
                        det.proj_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['precio'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
                    data = {'id': ingreso.id}
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Ingreso'
        context['entity'] = 'Ingresos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['det'] = []
        return context


class IngresoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Ingreso
    form_class = IngresoForm
    template_name = 'ingreso/create.html'
    success_url = reverse_lazy('erp:ingreso_list')
    permission_required = 'erp.change_ingreso'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Project.objects.filter(name__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item)
            elif action == 'edit':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    # sale = Sale.objects.get(pk=self.get_object().id)
                    ingreso = self.get_object()
                    ingreso.doc = vents['doc']
                    ingreso.date_joined = vents['date_joined']
                    ingreso.date_venc = vents['date_venc']
                    ingreso.cli_id = vents['cli']
                    ingreso.subtotal = float(vents['subtotal'])
                    ingreso.igv = float(vents['igv'])
                    ingreso.total = float(vents['total'])
                    ingreso.save()
                    ingreso.detsale_set.all().delete()
                    for i in vents['products']:
                        det = DetIngreso()
                        det.ingreso_id = ingreso.id
                        det.proj_id = i['id']
                        det.cant = int(i['cant'])
                        det.price = float(i['precio'])
                        det.subtotal = float(i['subtotal'])
                        det.save()
                    data = {'id': ingreso.id}
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_details_product(self):
        data = []
        try:
            for i in DetIngreso.objects.filter(ingreso_id=self.get_object().id):
                item = i.proj.toJSON()
                item['cant'] = i.cant
                data.append(item)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Ingreso'
        context['entity'] = 'Ingresos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['det'] = json.dumps(self.get_details_product())
        return context


class IngresoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Ingreso
    template_name = 'ingreso/delete.html'
    success_url = reverse_lazy('erp:ingreso_list')
    permission_required = 'erp.delete_ingreso'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Ingreso'
        context['entity'] = 'Ingresos'
        context['list_url'] = self.success_url
        return context


class IngresoInvoicePdfView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('ingreso/invoice.html')
            context = {
                'sale': Ingreso.objects.get(pk=self.kwargs['pk']),
                'comp': {'name': 'YURIÑA G.M.', 'ruc': '20605261176', 'address': 'Ate'},
                'icon': '{}{}'.format(settings.MEDIA_URL, 'img/logo1.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:ingreso_list'))

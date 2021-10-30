from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import EgresoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Egreso


class EgresoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Egreso
    template_name = 'egreso/list.html'
    permission_required = 'erp.view_egreso'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Egreso.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Diarios'
        context['create_url'] = reverse_lazy('erp:egreso_create')
        context['list_url'] = reverse_lazy('erp:egreso_list')
        context['entity'] = 'Egresos'
        return context


class EgresoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Egreso
    form_class = EgresoForm
    template_name = 'egreso/create.html'
    success_url = reverse_lazy('erp:egreso_list')
    permission_required = 'erp.add_egreso'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Diario Egreso'
        context['entity'] = 'Egresos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class EgresoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Egreso
    form_class = EgresoForm
    template_name = 'egreso/create.html'
    success_url = reverse_lazy('erp:egreso_list')
    permission_required = 'erp.change_egreso'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        # print(self.object)
        # print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Diario Egreso'
        context['entity'] = 'Egreso'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class EgresoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Egreso
    template_name = 'egreso/delete.html'
    success_url = reverse_lazy('erp:egreso_list')
    permission_required = 'erp.delete_egreso'
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
        context['title'] = 'Eliminación de Diario Egreso'
        context['entity'] = 'Egresos'
        context['list_url'] = self.success_url
        return context



# import json
# import os
#
# from django.conf import settings
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db import transaction
# from django.http import HttpResponse
# from django.http import JsonResponse, HttpResponseRedirect
# from django.template.loader import get_template
# from django.urls import reverse_lazy
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
# from xhtml2pdf import pisa
#
# from core.erp.forms import DiarioForm
# from core.erp.mixins import ValidatePermissionRequiredMixin
# from core.erp.models import Diario, DetDiario, Plancontable
#
#
# class DiarioListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
#     model = Diario
#     template_name = 'diario/list.html'
#     permission_required = 'erp.view_diario'
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'searchdata':
#                 data = []
#                 for i in Diario.objects.all():
#                     data.append(i.toJSON())
#             elif action == 'search_details_prod':
#                 data = []
#                 for i in DetDiario.objects.filter(diario_id=request.POST['id']):
#                     data.append(i.toJSON())
#             else:
#                 data['error'] = 'Ha ocurrido un error'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Libro Diario'
#         context['create_url'] = reverse_lazy('erp:diario_create')
#         context['list_url'] = reverse_lazy('erp:diario_list')
#         context['entity'] = 'Diarios'
#         return context
#
#
# class DiarioCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
#     model = Diario
#     form_class = DiarioForm
#     template_name = 'diario/create.html'
#     success_url = reverse_lazy('erp:diario_list')
#     permission_required = 'erp.add_diario'
#     url_redirect = success_url
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'search_products':
#                 data = []
#                 prods = Plancontable.objects.filter(name__icontains=request.POST['term'])[0:10]
#                 for i in prods:
#                     item = i.toJSON()
#                     # item['value'] = i.name
#                     item['text'] = i.name
#                     data.append(item)
#             elif action == 'add':
#                 with transaction.atomic():
#                     vents = json.loads(request.POST['vents'])
#                     diario = Diario()
#                     diario.nro = vents['nro']
#                     diario.ano = vents['ano']
#                     diario.mes = vents['mes']
#                     diario.date_joined = vents['date_joined']
#                     diario.desc = vents['desc']
#                     diario.impuestos = vents['impuestos']
#                     diario.debe = float(vents['debe'])
#                     diario.haber = float(vents['haber'])
#                     diario.save()
#                     for i in vents['plan']:
#                         det = DetDiario()
#                         det.diario_id = diario.id
#                         det.cuenta_id = i['id']
#                         det.debe = float(i['debe'])
#                         det.haber = float(i['haber'])
#                         det.save()
#                     data = {'id': diario.id}
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Creación de un Libro diario'
#         context['entity'] = 'Diarios'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         context['det'] = []
#         return context
#
#
# class DiarioUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
#     model = Diario
#     form_class = DiarioForm
#     template_name = 'diario/create.html'
#     success_url = reverse_lazy('erp:diario_list')
#     permission_required = 'erp.change_diario'
#     url_redirect = success_url
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'search_products':
#                 data = []
#                 prods = Plancontable.objects.filter(name__icontains=request.POST['term'])[0:10]
#                 for i in prods:
#                     item = i.toJSON()
#                     item['value'] = i.name
#                     data.append(item)
#             elif action == 'edit':
#                 with transaction.atomic():
#                     vents = json.loads(request.POST['vents'])
#                     # sale = Sale.objects.get(pk=self.get_object().id)
#                     diario = self.get_object()
#                     diario.date_joined = vents['date_joined']
#                     diario.nro = vents['nro']
#                     diario.desc = vents['desc']
#                     diario.impuestos = vents['impuestos']
#                     diario.debe = float(vents['debe'])
#                     diario.haber = float(vents['haber'])
#                     diario.save()
#                     diario.detdiario_set.all().delete()
#                     for i in vents['products']:
#                         det = DetDiario()
#                         det.diario_id = diario.id
#                         det.cuenta_id = i['id']
#                         det.debe = float(i['debe'])
#                         det.haber = float(i['haber'])
#                         det.save()
#                     data = {'id': diario.id}
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_details_product(self):
#         data = []
#         try:
#             for i in DetDiario.objects.filter(sale_id=self.get_object().id):
#                 item = i.cuenta.toJSON()
#                 item['debe'] = i.debe
#                 data.append(item)
#         except:
#             pass
#         return data
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Edición de Libro Diario'
#         context['entity'] = 'Diarios'
#         context['list_url'] = self.success_url
#         context['action'] = 'edit'
#         context['det'] = json.dumps(self.get_details_product())
#         return context
#
#
# class DiarioDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
#     model = Diario
#     template_name = 'diario/delete.html'
#     success_url = reverse_lazy('erp:diario_list')
#     permission_required = 'erp.delete_diario'
#     url_redirect = success_url
#
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Eliminación de Libro Diario'
#         context['entity'] = 'Diarios'
#         context['list_url'] = self.success_url
#         return context
#
#
# class DiarioInvoicePdfView(View):
#
#     def link_callback(self, uri, rel):
#         """
#         Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#         resources
#         """
#         # use short variable names
#         sUrl = settings.STATIC_URL  # Typically /static/
#         sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
#         mUrl = settings.MEDIA_URL  # Typically /static/media/
#         mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/
#
#         # convert URIs to absolute system paths
#         if uri.startswith(mUrl):
#             path = os.path.join(mRoot, uri.replace(mUrl, ""))
#         elif uri.startswith(sUrl):
#             path = os.path.join(sRoot, uri.replace(sUrl, ""))
#         else:
#             return uri  # handle absolute uri (ie: http://some.tld/foo.png)
#
#         # make sure that file exists
#         if not os.path.isfile(path):
#             raise Exception(
#                 'media URI must start with %s or %s' % (sUrl, mUrl)
#             )
#         return path
#
#     def get(self, request, *args, **kwargs):
#         try:
#             template = get_template('diario/invoice.html')
#             context = {
#                 'sale': Diario.objects.get(pk=self.kwargs['pk']),
#                 'comp': {'name': 'Jacman', 'ruc': '10104222043', 'address': 'Urbanización los ficus Calle Los pétalos 174, Santa Anita'},
#                 'icon': '{}{}'.format(settings.MEDIA_URL, '/logo1.png')
#             }
#             html = template.render(context)
#             response = HttpResponse(content_type='application/pdf')
#             # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#             pisaStatus = pisa.CreatePDF(
#                 html, dest=response,
#                 link_callback=self.link_callback
#             )
#             return response
#         except:
#             pass
#         return HttpResponseRedirect(reverse_lazy('erp:diario_list'))

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.forms import RentaActivoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import RentaActivo


class RentaActivoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = RentaActivo
    template_name = 'rentaactivo/list.html'
    permission_required = 'erp.view_rentaactivo'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in RentaActivo.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Rentabilidad sobre Activo'
        context['create_url'] = reverse_lazy('erp:rentaactivo_create')
        context['list_url'] = reverse_lazy('erp:rentaactivo_list')
        context['entity'] = 'RentaActivos'
        return context


class RentaActivoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin,CreateView):
    model = RentaActivo
    form_class = RentaActivoForm
    template_name = 'rentaactivo/create.html'
    success_url = reverse_lazy('erp:rentaactivo_list')
    permission_required = 'erp.add_rentaactivo'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                rentaactivo = 0
                for k in action['rentactivo']:
                    rentactivo = RentaActivo.objects.get(id=k['serial'])
                    subtotal = (rentactivo.utineta/rentactivo.actitotal) * 100
                    rentaactivo += subtotal
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Rentabilidad sobre Activo'
        context['entity'] = 'RentaActivos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class RentaActivoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = RentaActivo
    form_class = RentaActivoForm
    template_name = 'rentaactivo/create.html'
    success_url = reverse_lazy('erp:rentaactivo_list')
    permission_required = 'erp.change_rentaactivo'
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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Rentabilidad sobre Activo'
        context['entity'] = 'RentaActivos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class RentaActivoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = RentaActivo
    template_name = 'rentaactivo/delete.html'
    success_url = reverse_lazy('erp:rentaactivo_list')
    permission_required = 'erp.delete_rentaactivo'
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
        context['title'] = 'Eliminación de Rentabilidad sobre Activo'
        context['entity'] = 'RentaActivos'
        context['list_url'] = self.success_url
        return context
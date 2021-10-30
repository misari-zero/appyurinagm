from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.forms import EndfinancieroForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Endfinanciero


class EndfinancieroListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Endfinanciero
    template_name = 'endfinanciero/list.html'
    permission_required = 'erp.view_endfinanciero'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Endfinanciero.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Endeudamiento Financiero'
        context['create_url'] = reverse_lazy('erp:endfinanciero_create')
        context['list_url'] = reverse_lazy('erp:endfinanciero_list')
        context['entity'] = 'Endeudamiento'
        return context


class EndfinancieroCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin,CreateView):
    model = Endfinanciero
    form_class = EndfinancieroForm
    template_name = 'endfinanciero/create.html'
    success_url = reverse_lazy('erp:endfinanciero_list')
    permission_required = 'erp.add_endfinanciero'
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
        context['title'] = 'Endeudamiento Financiero'
        context['entity'] = 'Endeudemiento'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class EndfinancieroUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Endfinanciero
    form_class = EndfinancieroForm
    template_name = 'endfinanciero/create.html'
    success_url = reverse_lazy('erp:endfinanciero_list')
    permission_required = 'erp.change_endfinanciero'
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
        context['title'] = 'Endeudamiento Financiero'
        context['entity'] = 'Endeudamiento'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class EndfinancieroDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Endfinanciero
    template_name = 'endfinanciero/delete.html'
    success_url = reverse_lazy('erp:endfinanciero_list')
    permission_required = 'erp.delete_endfinanciero'
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
        context['title'] = 'Endeudamiento Financiero'
        context['entity'] = 'Endeudamiento'
        context['list_url'] = self.success_url
        return context
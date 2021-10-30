from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.forms import TipocuentaForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Tipocuenta


class TipocuentaListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Tipocuenta
    template_name = 'tipocuenta/list.html'
    permission_required = 'erp.view_tipocuenta'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Tipocuenta.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tipo cuenta'
        context['create_url'] = reverse_lazy('erp:tipocuenta_create')
        context['list_url'] = reverse_lazy('erp:tipocuenta_list')
        context['entity'] = 'Tipocuentas'
        return context


class TipocuentaCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Tipocuenta
    form_class = TipocuentaForm
    template_name = 'tipocuenta/create.html'
    success_url = reverse_lazy('erp:tipocuenta_list')
    permission_required = 'erp.add_tipocuenta'
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
        context['title'] = 'Creación de tipo cuenta'
        context['entity'] = 'Tipocuenta'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class TipocuentaUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Tipocuenta
    form_class = TipocuentaForm
    template_name = 'tipocuenta/create.html'
    success_url = reverse_lazy('erp:tipocuenta_list')
    permission_required = 'erp.change_tipocuenta'
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
        context['title'] = 'Edición de tipo cuenta'
        context['entity'] = 'Tipocuenta'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class TipocuentaDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Tipocuenta
    template_name = 'tipocuenta/delete.html'
    success_url = reverse_lazy('erp:tipocuenta_list')
    permission_required = 'erp.delete_tipocuenta'
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
        context['title'] = 'Eliminación de tipo cuenta'
        context['entity'] = 'Tipocuenta'
        context['list_url'] = self.success_url
        return context

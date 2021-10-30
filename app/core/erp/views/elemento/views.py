from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.forms import ElementoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Elemento


class ElementoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Elemento
    template_name = 'elemento/list.html'
    permission_required = 'erp.view_elemento'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Elemento.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Elementos'
        context['create_url'] = reverse_lazy('erp:elemento_create')
        context['list_url'] = reverse_lazy('erp:elemento_list')
        context['entity'] = 'Elementos'
        return context


class ElementoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Elemento
    form_class = ElementoForm
    template_name = 'elemento/create.html'
    success_url = reverse_lazy('erp:elemento_list')
    permission_required = 'erp.add_elemento'
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
        context['title'] = 'Creación de elementos'
        context['entity'] = 'Elemento'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ElementoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Elemento
    form_class = ElementoForm
    template_name = 'elemento/create.html'
    success_url = reverse_lazy('erp:elemento_list')
    permission_required = 'erp.change_elemento'
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
        context['title'] = 'Edición de elementos'
        context['entity'] = 'Elemento'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ElementoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Elemento
    template_name = 'elemento/delete.html'
    success_url = reverse_lazy('erp:elemento_list')
    permission_required = 'erp.delete_elemento'
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
        context['title'] = 'Eliminación de elementos'
        context['entity'] = 'Elementos'
        context['list_url'] = self.success_url
        return context

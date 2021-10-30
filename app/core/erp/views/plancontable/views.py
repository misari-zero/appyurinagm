from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.forms import PlancontableForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Plancontable


class PlancontableListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Plancontable
    template_name = 'plancontable/list.html'
    permission_required = 'erp.view_plancontable'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Plancontable.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Plan contable'
        context['create_url'] = reverse_lazy('erp:plancontable_create')
        context['list_url'] = reverse_lazy('erp:plancontable_list')
        context['entity'] = 'Plancontables'
        return context


class PlancontableCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Plancontable
    form_class = PlancontableForm
    template_name = 'plancontable/create.html'
    success_url = reverse_lazy('erp:plancontable_list')
    permission_required = 'erp.add_plancontable'
    url_redirect = success_url

    @method_decorator(login_required)
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
        context['title'] = 'Creación de plan contable'
        context['entity'] = 'Plancontable'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class PlancontableUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Plancontable
    form_class = PlancontableForm
    template_name = 'plancontable/create.html'
    success_url = reverse_lazy('erp:plancontable_list')
    permission_required = 'erp.change_plancontable'
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
        context['title'] = 'Edición de plan contable'
        context['entity'] = 'Plancontables'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class PlancontableDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Plancontable
    template_name = 'plancontable/delete.html'
    success_url = reverse_lazy('erp:plancontable_list')
    permission_required = 'erp.delete_plancontable'
    url_redirect = success_url

    @method_decorator(login_required)
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
        context['title'] = 'Eliminación de plan contable'
        context['entity'] = 'Plancontables'
        context['list_url'] = self.success_url
        return context

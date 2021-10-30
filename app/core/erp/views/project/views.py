from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from core.erp.forms import ProjectForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Proveedor, Project


class ProjectListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Project
    template_name = 'project/list.html'
    permission_required = 'erp.view_project'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Project.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Proyectos'
        context['create_url'] = reverse_lazy('erp:project_create')
        context['list_url'] = reverse_lazy('erp:project_list')
        context['entity'] = 'Proyectos'
        return context


class ProjectCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin,CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('erp:project_list')
    permission_required = 'erp.add_project'
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
        context['title'] = 'Creación de proyectos'
        context['entity'] = 'Proyectos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ProjectUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('erp:project_list')
    permission_required = 'erp.change_project'
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
        context['title'] = 'Edición de Proyectos'
        context['entity'] = 'Proyectos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ProjectDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('erp:project_list')
    permission_required = 'erp.delete_project'
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
        context['title'] = 'Eliminación de Proyectos'
        context['entity'] = 'Proyectos'
        context['list_url'] = self.success_url
        return context
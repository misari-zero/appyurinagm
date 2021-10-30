from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

# from core.erp.forms import ComprobanteingresoForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Plancontable


# class ComprobanteingresoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
#     model = Comprobanteingreso
#     form_class = ComprobanteingresoForm
#     template_name = 'comprobanteingreso/create.html'
#     success_url = reverse_lazy('index')
#     permission_required = 'erp.add_comprobanteingreso'
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
#             if action == 'search_contable':
#                 data = []
#                 plancont = Plancontable.objects.filter(name__icontains=request.POST['term'])
#                 for i in plancont:
#                     item = i.toJSON()
#                     item['value'] = i.name
#                     data.append(item)
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Creación de Comprobante diario'
#         context['entity'] = 'Comprobanteingreso'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         return context
from django.urls import path
from core.erp.views.client.views import *
from core.erp.views.comprobanteingreso.views import *
from core.erp.views.dashboard.views import *
from core.erp.views.diario.views import *
from core.erp.views.egreso.views import *
from core.erp.views.elemento.views import *
from core.erp.views.endfinanciero.views import *
from core.erp.views.ingreso.views import IngresoListView, IngresoCreateView, IngresoDeleteView, IngresoUpdateView, \
    IngresoInvoicePdfView
from core.erp.views.mayor.views import *
from core.erp.views.plancontable.views import *
from core.erp.views.product.views import *
from core.erp.views.categoria.views import *
from core.erp.views.project.views import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from core.erp.views.proveedor.views import ProveedorListView, ProveedorCreateView, ProveedorUpdateView, \
    ProveedorDeleteView
from core.erp.views.tipocuenta.views import *
from core.erp.views.sale.views import SaleListView, \
    SaleCreateView, SaleDeleteView, SaleUpdateView, SaleInvoicePdfView

app_name = 'erp'

urlpatterns = [
    # client
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    # path('client/form/', ClientFormView.as_view(), name='client_form'),
    # proveedor
    path('proveedor/list/', ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedor/add/', ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedor/update/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('proveedor/delete/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_delete'),
    # project
    path('project/list/', ProjectListView.as_view(), name='project_list'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    # elemento
    path('elemento/list/', ElementoListView.as_view(), name='elemento_list'),
    path('elemento/add/', ElementoCreateView.as_view(), name='elemento_create'),
    path('elemento/update/<int:pk>/', ElementoUpdateView.as_view(), name='elemento_update'),
    path('elemento/delete/<int:pk>/', ElementoDeleteView.as_view(), name='elemento_delete'),
    # tipocuenta
    path('tipocuenta/list/', TipocuentaListView.as_view(), name='tipocuenta_list'),
    path('tipocuenta/add/', TipocuentaCreateView.as_view(), name='tipocuenta_create'),
    path('tipocuenta/update/<int:pk>/', TipocuentaUpdateView.as_view(), name='tipocuenta_update'),
    path('tipocuenta/delete/<int:pk>/', TipocuentaDeleteView.as_view(), name='tipocuenta_delete'),
    # plancontable
    path('plancontable/list/', PlancontableListView.as_view(), name='plancontable_list'),
    path('plancontable/add/', PlancontableCreateView.as_view(), name='plancontable_create'),
    path('plancontable/update/<int:pk>/', PlancontableUpdateView.as_view(), name='plancontable_update'),
    path('plancontable/delete/<int:pk>/', PlancontableDeleteView.as_view(), name='plancontable_delete'),
    # categoria
    path('categoria/list/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/add/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/update/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/delete/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    # sale
    path('sale/list/', SaleListView.as_view(), name='sale_list'),
    path('sale/add/', SaleCreateView.as_view(), name='sale_create'),
    path('sale/delete/<int:pk>/', SaleDeleteView.as_view(), name='sale_delete'),
    path('sale/update/<int:pk>/', SaleUpdateView.as_view(), name='sale_update'),
    path('sale/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # comprobanteingreso
    # path('comprobanteingreso/add/', ComprobanteingresoCreateView.as_view(), name='comprobanteingreso_create'),
    # diario
    path('diario/list/', DiarioListView.as_view(), name='diario_list'),
    path('diario/add/', DiarioCreateView.as_view(), name='diario_create'),
    path('diario/delete/<int:pk>/', DiarioDeleteView.as_view(), name='diario_delete'),
    path('diario/update/<int:pk>/', DiarioUpdateView.as_view(), name='diario_update'),
    # path('diario/invoice/pdf/<int:pk>/', DiarioInvoicePdfView.as_view(), name='diario_invoice_pdf'),
    # egreso
    path('egreso/list/', EgresoListView.as_view(), name='egreso_list'),
    path('egreso/add/', EgresoCreateView.as_view(), name='egreso_create'),
    path('egreso/delete/<int:pk>/', EgresoDeleteView.as_view(), name='egreso_delete'),
    path('egreso/update/<int:pk>/', EgresoUpdateView.as_view(), name='egreso_update'),
    # mayor
    path('mayor/list/', MayorListView.as_view(), name='mayor_list'),
    path('mayor/add/', MayorCreateView.as_view(), name='mayor_create'),
    path('mayor/delete/<int:pk>/', MayorDeleteView.as_view(), name='mayor_delete'),
    path('mayor/update/<int:pk>/', MayorUpdateView.as_view(), name='mayor_update'),
    # ingreso
    path('ingreso/list/', IngresoListView.as_view(), name='ingreso_list'),
    path('ingreso/add/', IngresoCreateView.as_view(), name='ingreso_create'),
    path('ingreso/delete/<int:pk>/', IngresoDeleteView.as_view(), name='ingreso_delete'),
    path('ingreso/update/<int:pk>/', IngresoUpdateView.as_view(), name='ingreso_update'),
    path('ingreso/invoice/pdf/<int:pk>/', IngresoInvoicePdfView.as_view(), name='ingreso_invoice_pdf'),
    # egreso
    path('endfinanciero/list/', EndfinancieroListView.as_view(), name='endfinanciero_list'),
    path('endfinanciero/add/', EndfinancieroCreateView.as_view(), name='endfinanciero_create'),
    path('endfinanciero/delete/<int:pk>/', EndfinancieroDeleteView.as_view(), name='endfinanciero_delete'),
    path('endfinanciero/update/<int:pk>/', EndfinancieroUpdateView.as_view(), name='endfinanciero_update'),
]

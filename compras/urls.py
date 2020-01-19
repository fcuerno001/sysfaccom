from django.urls import path

from .views import ProveedorView, ProveedorNew, ProveedorEdit, proveedor_inactivar

urlpatterns = [
    path('Proveedores/',ProveedorView.as_view(),name="proveedor_list"),
    path('Proveedores/new',ProveedorNew.as_view(),name="proveedor_new"),
    path('Proveedores/edit/<int:pk>',ProveedorEdit.as_view(),name="proveedor_edit"),
    path('Proveedores/inactivar/<int:id>',proveedor_inactivar,name="proveedor_inactivar"),

]
    
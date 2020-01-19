from django.urls import path

from .views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDel, SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDel,   \
    MarcaView, MarcaNew, MarcaEdit, marca_inactivar, UnidadMView,UnidadMNew, UnidadMEdit, unidadm_inactivar, ProductoView,ProductoNew,ProductoEdit, \
        ProductoDel, producto_inactivar
    

urlpatterns = [
    path('categorias/',CategoriaView.as_view(),name="categoria_list"),
    path('categorias/new',CategoriaNew.as_view(),name="categoria_new"),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(),name="categoria_edit"),
    path('categorias/delete/<int:pk>',CategoriaDel.as_view(),name="categoria_del"),

    path('subcategorias/',SubCategoriaView.as_view(),name="subcategoria_list"),
    path('subcategorias/new',SubCategoriaNew.as_view(),name="subcategoria_new"),
    path('subcategorias/edit/<int:pk>',SubCategoriaEdit.as_view(),name="subcategoria_edit"),
    path('subcategorias/delete/<int:pk>',SubCategoriaDel.as_view(),name="subcategoria_del"),


    path('Marca/',MarcaView.as_view(),name="marca_list"),
    path('Marca/new',MarcaNew.as_view(),name="marca_new"),
    path('Marca/edit/<int:pk>',MarcaEdit.as_view(),name="marca_edit"),
    path('Marca/inactivar/<int:id>',marca_inactivar,name="marca_inactivar"),

    path('UnidadMedida/',UnidadMView.as_view(),name="unidadm_list"),
    path('UnidadMedida/new',UnidadMNew.as_view(),name="unidadm_new"),
    path('UnidadMedida/edit/<int:pk>',UnidadMEdit.as_view(),name="unidadm_edit"),
    path('UnidadMedida/inactivar/<int:id>',unidadm_inactivar,name="unidadm_inactivar"),

    path('Productos/',ProductoView.as_view(),name="producto_list"),
    path('Productos/new',ProductoNew.as_view(),name="producto_new"),
    path('Productos/edit/<int:pk>',ProductoEdit.as_view(),name="producto_edit"),
    path('Productos/inactivar/<int:id>',producto_inactivar,name="producto_inactivar"),


]

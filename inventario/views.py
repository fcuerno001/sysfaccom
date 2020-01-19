from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy #Reenviarnos al sitio seleccionado.
# Create your views here.

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMForm, ProductoForm

class CategoriaView(LoginRequiredMixin, generic.ListView ):
    model = Categoria
    template_name = "inventario/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

#Metodo para guardar el formulario Categoria
class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model=Categoria
    template_name="inventario/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inventario:categoria_list")
    
    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model=Categoria
    template_name="inventario/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inventario:categoria_list")
    
    def form_valid(self, form):
        form.instance.usuario_modif = self.request.user.id
        return super().form_valid(form)


class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model=Categoria
    template_name='inventario/categoria_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inventario:categoria_list")


class SubCategoriaView(LoginRequiredMixin, generic.ListView ):
    model = SubCategoria
    template_name = 'inventario/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'


#Metodo para guardar el formulario Sub Categoria
class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model=Categoria
    template_name="inventario/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inventario:subcategoria_list")
    
    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)


class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model=SubCategoria
    template_name="inventario/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inventario:subcategoria_list")
    
    def form_valid(self, form):
        form.instance.usuario_modif = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.DeleteView):
    model=SubCategoria
    template_name='inventario/subcategoria_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inventario:subcategoria_list")


class MarcaView(LoginRequiredMixin, generic.ListView ):
    model = Marca
    template_name = "inventario/marca_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

#Metodo para guardar el formulario Marca
class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model=Marca
    template_name="inventario/marca_form.html"
    context_object_name = "obj"
    form_class=MarcaForm
    success_url=reverse_lazy("inventario:marca_list")
    
    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model=Marca
    template_name="inventario/marca_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inventario:marca_list")
    
    def form_valid(self, form):
        form.instance.usuario_modif = self.request.user.id
        return super().form_valid(form)

def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name="inventario/categoria_del.html"

    if not marca:
        return redirect("inventario:marca_list")

    if request.method=='GET':
        contexto={'obj':marca}

    if request.method=='POST':
        marca.estado=False
        marca.save()
        return redirect("inventario:marca_list")

    return render(request,template_name,contexto)


class UnidadMView(LoginRequiredMixin, generic.ListView ):
    model = UnidadMedida
    template_name = "inventario/unidadm_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

#Metodo para guardar el formulario Unidad de Medida
class UnidadMNew(LoginRequiredMixin, generic.CreateView):
    model=UnidadMedida
    template_name="inventario/unidadm_form.html"
    context_object_name = "obj"
    form_class=UnidadMForm
    success_url=reverse_lazy("inventario:unidadm_list")
    
    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)

class UnidadMEdit(LoginRequiredMixin, generic.UpdateView):
    model=UnidadMedida
    template_name="inventario/unidad_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inventario:unidadm_list")
    
    def form_valid(self, form):
        form.instance.usuario_modif = self.request.user.id
        return super().form_valid(form)

def unidadm_inactivar(request, id):
    unidadm = UnidadMedida.objects.filter(pk=id).first()
    contexto={}
    template_name="inventario/categoria_del.html"

    if not marca:
        return redirect("inventario:unidadm_list")

    if request.method=='GET':
        contexto={'obj':marca}

    if request.method=='POST':
        marca.estado=False
        marca.save()
        return redirect("inventario:unidadm_list")

    return render(request,template_name,contexto)
    
class ProductoView(LoginRequiredMixin, generic.ListView ):
    model = Producto
    template_name = "inventario/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

#Metodo para guardar el formulario Producto
class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model=Producto
    template_name="inventario/producto_form.html"
    context_object_name = "obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inventario:producto_list")
    
    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model=Producto
    template_name="inventario/producto_form.html"
    context_object_name = "obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inventario:producto_list")
    
    def form_valid(self, form):
        form.instance.usuario_modif = self.request.user.id
        return super().form_valid(form)

def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inventario/producto_del.html"

    if not Producto:
        return redirect("inventario:producto_list")

    if request.method=='GET':
        contexto={'obj':Producto}

    if request.method=='POST':
        producto.estado=False
        producto.save()
        return redirect("inventario:producto_list")

    return render(request,template_name,contexto)


class ProductoDel(LoginRequiredMixin, generic.DeleteView):
    model=Producto
    template_name='inventario/producto_del.html'
    context_object_name='obj'
    success_url=reverse_lazy("inventario:producto_list")
    
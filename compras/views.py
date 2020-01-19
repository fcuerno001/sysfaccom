from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy #Reenviarnos al sitio seleccionado.
from django.http import HttpResponse
import json

from .models import Proveedor
from  compras.forms import ProveedorForm

class ProveedorView(LoginRequiredMixin, generic.ListView ):
    model = Proveedor
    template_name = "compras/proveedor_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

#Metodo para guardar el formulario Producto
class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model=Proveedor
    template_name="compras/proveedor_form.html"
    context_object_name = "obj"
    form_class=ProveedorForm
    success_url=reverse_lazy("compras:proveedor_list")
    
    def form_valid(self, form):
        form.instance.usuario_crea = self.request.user
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model=Proveedor
    template_name="compras/proveedor_form.html"
    context_object_name = "obj"
    form_class=ProveedorForm
    success_url=reverse_lazy("compras:proveedor_list")
    
    def form_valid(self, form):
        form.instance.usuario_modif = self.request.user.id
        return super().form_valid(form)

def proveedor_inactivar(request, id):
    proveedor = Proveedor.objects.filter(pk=id).first()
    contexto={}
    template_name="compras/proveedor_del.html"

    if not proveedor:
        return HttpResponse('Proveedor no existe' + str(id))

    if request.method=='GET':
        contexto={'obj':proveedor}
    
    if request.method=='POST':
        proveedor.estado=False
        proveedor.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')
        
    return render(request,template_name,contexto)


from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modif = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract=True
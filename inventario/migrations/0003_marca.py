# Generated by Django 2.2.6 on 2019-10-28 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0002_subcategoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
                ('usuario_modif', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(help_text='Descripcion de la Marca', max_length=100, unique=True)),
                ('usuario_crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Marca',
            },
        ),
    ]
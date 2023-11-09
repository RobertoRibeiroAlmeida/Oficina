from django.contrib import admin
from .models import Marca, Modelo, Cliente, Veiculo

admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Cliente)
admin.site.register(Veiculo)

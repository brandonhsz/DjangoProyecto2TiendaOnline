from django.contrib import admin
from gestionPedidos.models import Clients, Items, Order

# Register your models here
admin.site.register(Clients)
admin.site.register(Items)
admin.site.register(Order)
from http import client
from django.contrib import admin
from Vendas.models import cliente, produtos, encomenda

# Register your models here.

admin.site.register(cliente)
admin.site.register(produtos)
admin.site.register(encomenda)
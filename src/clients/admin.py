from django.contrib import admin
from .models import Clients


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email']
    search_fields = ['name']

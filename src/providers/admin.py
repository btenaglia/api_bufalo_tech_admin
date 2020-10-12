from django.contrib import admin
from .models import Providers


@admin.register(Providers)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email']
    search_fields = ['name']

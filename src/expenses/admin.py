from django.contrib import admin
from .models import Types


@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']

from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    """Настройки админки для услуг."""
    list_display = ("pk", "name", "cost")
    list_display_links = ("name",)
    search_fields = ("name",)

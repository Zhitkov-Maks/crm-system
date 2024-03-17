from django.contrib import admin
from .models import Customers


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    """Настройки админки для Активных клиентов."""
    list_display = ("id", "lead", "contract")
    autocomplete_fields = ("lead", "contract")
    list_display_links = ("id", "lead")

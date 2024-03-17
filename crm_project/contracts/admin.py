from django.contrib import admin
from .models import Contracts


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    """Настройки админки для контрактов."""
    list_display: tuple = "id", "name", "product", "start_date", "end_date", "cost"
    list_display_links: tuple = "id", "name"
    autocomplete_fields: list = ["product"]
    search_fields: list = ["name"]

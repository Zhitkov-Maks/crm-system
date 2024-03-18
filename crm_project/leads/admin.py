from django.contrib import admin
from .models import Leads


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    """Настраиваем админ панель для потенциальных клиентов."""
    list_display = ("pk", "last_name", "first_name", "middle_name", "email", "phone", "advertising")
    list_display_links = ("last_name", "first_name")
    search_fields = ("last_name",)
    autocomplete_fields = ("advertising",)

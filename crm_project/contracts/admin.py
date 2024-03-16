from django.contrib import admin
from .models import Contracts


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"

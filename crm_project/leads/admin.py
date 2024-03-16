from django.contrib import admin
from .models import Leads


@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    list_display = ("pk", "last_name", "first_name")
    list_display_links = ("last_name", "first_name")
    search_fields = ("last_name",)

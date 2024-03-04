from django.contrib import admin
from .models import Customers


@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'lead')
    list_display_links = ('id', 'lead')

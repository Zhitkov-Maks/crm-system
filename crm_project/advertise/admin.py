from django.contrib import admin
from .models import Advertise


@admin.register(Advertise)
class AdvertiseAdmin(admin.ModelAdmin):
    list_display: tuple = ('id', 'name', 'budget')
    list_display_links: tuple = ('id', 'name')

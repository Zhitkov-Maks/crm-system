from django.urls import path
from .views import IndexView


urlpatterns: list = [path("", IndexView.as_view(), name="index")]

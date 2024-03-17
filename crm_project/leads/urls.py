from django.urls import path
from .views import (
    ListLeads,
    DetailLeads,
    DeleteLeads,
    CreateLeads,
    UpdateLeads,
    ListLeadsSearch,
)

urlpatterns: list = [
    path("", ListLeads.as_view(), name="list-leads"),
    path("<int:pk>/", DetailLeads.as_view(), name="detail-leads"),
    path("<int:pk>/delete/", DeleteLeads.as_view(), name="delete-leads"),
    path("<int:pk>/edit/", UpdateLeads.as_view(), name="update-leads"),
    path("new/", CreateLeads.as_view(), name="create-leads"),
    path("search/", ListLeadsSearch.as_view(), name="search-leads"),
]

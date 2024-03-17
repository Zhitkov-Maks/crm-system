from django.urls import path
from .views import (
    CustomerList,
    CustomerDetail,
    CustomerUpdate,
    CustomerCreate,
    CustomerDelete,
    CustomersSearch,
)


urlpatterns: list = [
    path("", CustomerList.as_view(), name="customer-list"),
    path("<int:pk>/edit/", CustomerUpdate.as_view(), name="customer-edit"),
    path("<int:pk>/", CustomerDetail.as_view(), name="customer-detail"),
    path("new/", CustomerCreate.as_view(), name="customer-create"),
    path("<int:pk>/delete/", CustomerDelete.as_view(), name="customer-delete"),
    path("search/", CustomersSearch.as_view(), name="customers-search"),
]

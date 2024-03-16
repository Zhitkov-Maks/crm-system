from django.urls import path
from .views import (
    CreateContract,
    ListContract,
    UpdateContract,
    DeleteContract,
    DetailContract,
    ContractsSearch
)

urlpatterns: list = [
    path("new/", CreateContract.as_view(), name="create-contract"),
    path("", ListContract.as_view(), name="list-contracts"),
    path("<int:pk>/edit/", UpdateContract.as_view(), name="update-contracts"),
    path("<int:pk>/delete/", DeleteContract.as_view(), name="delete-contracts"),
    path("<int:pk>/", DetailContract.as_view(), name="detail-contracts"),
    path("search/", ContractsSearch.as_view(), name="contracts-search"),
]

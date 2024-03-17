from django.urls import path
from .views import (
    ListProducts,
    DetailProducts,
    DeleteProducts,
    CreateProducts,
    UpdateProducts,
    ProductsSearch
)


urlpatterns: list = [
    path("", ListProducts.as_view(), name="list-product"),
    path("<int:pk>/", DetailProducts.as_view(), name="detail-product"),
    path("<int:pk>/delete/", DeleteProducts.as_view(), name="delete-product"),
    path("<int:pk>/edit/", UpdateProducts.as_view(), name="update-product"),
    path("new/", CreateProducts.as_view(), name="create-product"),
    path("search/", ProductsSearch.as_view(), name="search-products")
]

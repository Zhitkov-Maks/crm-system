from django.urls import path
from .views import ListProducts, DetailProducts, DeleteProducts, CreateProducts, UpdateProducts


urlpatterns = [
    path('', ListProducts.as_view(), name='list-view'),
    path('<int:pk>/', DetailProducts.as_view(), name='detail-view'),
    path('<int:pk>/delete/', DeleteProducts.as_view(), name='delete-view'),
    path('<int:pk>/edit/', UpdateProducts.as_view(), name='update-view'),
    path('new/', CreateProducts.as_view(), name='create-view'),
]

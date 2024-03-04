from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Products
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ListProducts(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'products.view_products'
    template_name = 'products/products-list.html'
    model = Products
    context_object_name = 'products'


class DetailProducts(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'products.view_products'
    template_name = 'products/products-detail.html'
    model = Products


class DeleteProducts(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'products.delete_products'
    template_name = 'products/products-delete.html'
    model = Products
    success_url = '/products/'


class UpdateProducts(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'products.change_products'
    template_name = 'products/products-edit.html'
    fields = 'name', 'description', 'cost'
    model = Products
    success_url = '/products/'


class CreateProducts(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'products.add_products'
    template_name = 'products/products-create.html'
    fields = 'name', 'description', 'cost'
    success_url = '/products/'
    model = Products

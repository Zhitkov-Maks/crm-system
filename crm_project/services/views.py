from ast import List
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Products


class ListProducts(ListView):
    template_name = 'products/products-list.html'
    model = Products
    context_object_name = 'products'


class DetailProducts(DetailView):
    template_name = 'products/products-detail.html'
    model = Products


class DeleteProducts(DeleteView):
    template_name = 'products/products-delete.html'
    model = Products


class UpdateProducts(UpdateView):
    template_name = 'products/products-edit.html'
    fields = 'name', 'description', 'cost'
    model = Products
    success_url = '/products/'


class CreateProducts(CreateView):
    template_name = 'products/products-create.html'
    fields = 'name', 'description', 'cost'
    success_url = '/products/'
    model = Products

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customers


class CustomerList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'customers.view_customers'
    template_name = 'customers/customers-list.html'
    model = Customers
    context_object_name = 'customers'


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'customers.view_customers'
    template_name = 'customers/customers-detail.html'
    model = Customers


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'customers.add_customers'
    template_name = 'customers/customers-create.html'
    model = Customers
    fields = 'lead',
    success_url = '/customers/'


class CustomerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'customers.change_customers'
    template_name = 'customers/customers-edit.html'
    model = Customers
    fields = 'lead',
    success_url = '/customers/'


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'customers.delete_customers'
    template_name = 'customers/customers-delete.html'
    model = Customers
    success_url = '/customers/'

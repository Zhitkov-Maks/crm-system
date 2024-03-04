from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Contracts


class CreateContract(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'contracts.add_contracts'
    template_name = 'contracts/contracts-create.html'
    model = Contracts
    fields = 'name', 'product', 'start_date', 'end_date', 'cost', 'file'
    success_url = '/contracts/'


class ListContract(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'contracts.view_contracts'
    template_name = 'contracts/contracts-list.html'
    model = Contracts
    context_object_name = 'contracts'


class UpdateContract(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'contracts.change_contracts'
    template_name = 'contracts/contracts-edit.html'
    model = Contracts
    fields = 'name', 'product', 'start_date', 'end_date', 'cost', 'file'
    success_url = '/contracts/'


class DetailContract(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'contracts.view_contracts'
    template_name = 'contracts/contracts-detail.html'
    model = Contracts


class DeleteContract(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'contracts.delete_contracts'
    template_name = 'contracts/contracts-delete.html'
    model = Contracts
    success_url = '/contracts/'

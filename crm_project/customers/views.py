from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import QuerySet, Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Customers
from .form import CustomerForm


class CustomerList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "customers.view_customers"
    template_name = "customers/customers-list.html"
    model = Customers
    context_object_name = "customers"

    def get_queryset(self):
        return (
            Customers.objects.select_related("lead")
            .all()
            .order_by("lead__last_name", "lead__first_name")
        )


class CustomersSearch(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "customers.view_customers"
    template_name = "customers/customers-list.html"
    model = Customers
    context_object_name = "customers"

    def get_queryset(self) -> QuerySet:
        """Переопределяем метод для поиска клиента по фамилии"""
        query = self.request.GET.get("query")
        return (
            Customers.objects.select_related("lead")
            .filter(Q(lead__last_name__iregex=query))
            .order_by("lead__last_name", "lead__first_name")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет идентификатор для отображения сортировки в шаблоне"""
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "customers.view_customers"
    template_name = "customers/customers-detail.html"
    model = Customers


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "customers.add_customers"
    template_name = "customers/customers-create.html"
    model = Customers
    form_class = CustomerForm
    success_url = "/customers/"


class CustomerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "customers.change_customers"
    template_name = "customers/customers-edit.html"
    model = Customers
    fields = "lead", "contract"
    success_url = "/customers/"


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "customers.delete_customers"
    template_name = "customers/customers-delete.html"
    model = Customers
    success_url = "/customers/"

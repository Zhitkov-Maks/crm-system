from typing import Any

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
    """Класс для отображения списка Активных клиентов."""
    permission_required: str = "customers.view_customers"
    template_name: str = "customers/customers-list.html"
    model: Any = Customers
    context_object_name: str = "customers"

    def get_queryset(self) -> QuerySet:
        """
        Переопределил метод, для загрузки всех нужных данных сразу, тем самым избегая множества
        дополнительных запросов к базе.
        """
        return (
            Customers.objects.select_related("lead")
            .all()
            .order_by("lead__last_name", "lead__first_name")
        )


class CustomersSearch(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Класс для поиска Активных клиентов по фамилии."""
    permission_required: str = "customers.view_customers"
    template_name: str = "customers/customers-list.html"
    model: Any = Customers
    context_object_name: str = "customers"

    def get_queryset(self) -> QuerySet:
        """Переопределяем метод для поиска клиента по фамилии, без учета регистра."""
        query = self.request.GET.get("query")
        return (
            Customers.objects.select_related("lead")
            .filter(Q(lead__last_name__iregex=query))
            .order_by("lead__last_name", "lead__first_name")
        )

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        """Добавляет идентификатор для отображения ввода пользователя в шаблоне."""
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class CustomerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс для отображения детальной информации об активном клиенте."""
    permission_required: str = "customers.view_customers"
    template_name: str = "customers/customers-detail.html"
    model: Any = Customers


class CustomerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс для создания нового активного клиента."""
    permission_required: str = "customers.add_customers"
    template_name: str = "customers/customers-create.html"
    model: Any = Customers
    form_class: Any = CustomerForm
    success_url: str = "/customers/"


class CustomerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс для изменения активного клиента."""
    permission_required: str = "customers.change_customers"
    template_name: str = "customers/customers-edit.html"
    model: Any = Customers
    fields: tuple = "lead", "contract"
    success_url: str = "/customers/"


class CustomerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # type: ignore
    """
    Класс для удаления активного клиента. Комментарий type: ignore нужен для mypy,
    который прокидывает ошибку
    'Definition of "object" in base class "DeletionMixin" is
    incompatible with definition in base class "BaseDetailView"'.
    """
    permission_required: str = "customers.delete_customers"
    template_name: str = "customers/customers-delete.html"
    model: Any = Customers
    success_url: str = "/customers/"

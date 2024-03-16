from typing import Any
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q, QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)

from .models import Contracts
from .form import ContractForm


class CreateContract(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс для создания контракта."""
    permission_required: str = "contracts.add_contracts"
    template_name: str = "contracts/contracts-create.html"
    model: Any = Contracts
    form_class: Any = ContractForm
    success_url: str = "/contracts/"

    def form_valid(self, form) -> HttpResponse:
        """
        Дополнительно проверяем корректность ввода даты,
        чтобы дата окончания была больше чем дата начала.
        """
        if form.is_valid():
            start_date: date = form.cleaned_data["start_date"]
            end_date: date = form.cleaned_data["end_date"]
            if start_date < end_date:
                form.save()
                return redirect("list-contracts")
            form.add_error(
                "end_date", "Дата окончания меньше чем дата начала контракта."
            )
        return render(
            self.request, "contracts/contracts-create.html", context={"form": form}
        )


class ContractsSearch(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Класс для поиска контракта по названию. Поиск осуществляется по вхождению подстроки в строке
    без учета регистра.
    """
    permission_required: str = "contracts.view_contracts"
    template_name: str = "contracts/contracts-list.html"
    model: Any = Contracts
    context_object_name: str = "contracts"

    def get_queryset(self) -> QuerySet:
        """Переопределяем метод для поиска контракта по названию."""
        query = self.request.GET.get("query")
        return (
            Contracts.objects.filter(Q(name__iregex=query)).order_by("-start_date")
        )

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        """
        Добавляет идентификатор для отображения введенного
        пользователем сообщения для поиска.
        """
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class ListContract(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """Класс для получения списка контрактов."""
    permission_required: str = "contracts.view_contracts"
    template_name: str = "contracts/contracts-list.html"
    model: Any = Contracts
    context_object_name: str = "contracts"


class UpdateContract(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Класс для изменения данных о контракте."""
    permission_required: str = "contracts.change_contracts"
    template_name: str = "contracts/contracts-edit.html"
    model: Any = Contracts
    form_class: Any = ContractForm
    success_url: str = "/contracts/"


class DetailContract(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Класс для отображения детальной информации о контракте."""
    permission_required: str = "contracts.view_contracts"
    template_name: str = "contracts/contracts-detail.html"
    model: Any = Contracts


class DeleteContract(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # type: ignore
    """
    Класс для удаления контракта. Комментарий type: ignore нужен для mypy,
    который прокидывает ошибку
    'Definition of "object" in base class "DeletionMixin" is
    incompatible with definition in base class "BaseDetailView"'.
    """
    permission_required: str = "contracts.delete_contracts"
    template_name: str = "contracts/contracts-delete.html"
    model: Any = Contracts
    success_url: str = "/contracts/"

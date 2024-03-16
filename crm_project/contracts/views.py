from urllib.request import Request
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Count, Q, QuerySet
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
    permission_required = "contracts.add_contracts"
    template_name = "contracts/contracts-create.html"
    model = Contracts
    form_class = ContractForm
    success_url = "/contracts/"

    def form_valid(self, form) -> HttpResponse:
        """
        Дополнительно проверяем корректность ввода даты,
        чтобы дата окончания была больше чем дата начала.
        """
        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]
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
    permission_required = "contracts.view_contracts"
    template_name = "contracts/contracts-list.html"
    model = Contracts
    context_object_name = "contracts"

    def get_queryset(self) -> QuerySet:
        """Переопределяем метод для поиска клиента по фамилии"""
        query = self.request.GET.get("query")
        return (
            Contracts.objects.filter(Q(name__iregex=query)).order_by("-start_date")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет идентификатор для отображения сортировки в шаблоне"""
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class ListContract(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "contracts.view_contracts"
    template_name = "contracts/contracts-list.html"
    model = Contracts
    context_object_name = "contracts"


class UpdateContract(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "contracts.change_contracts"
    template_name = "contracts/contracts-edit.html"
    model = Contracts
    form_class = ContractForm
    success_url = "/contracts/"


class DetailContract(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "contracts.view_contracts"
    template_name = "contracts/contracts-detail.html"
    model = Contracts


class DeleteContract(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "contracts.delete_contracts"
    template_name = "contracts/contracts-delete.html"
    model = Contracts
    success_url = "/contracts/"

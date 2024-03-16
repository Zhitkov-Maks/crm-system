from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q, QuerySet
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Leads


class ListLeads(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "leads.view_leads"
    template_name = "leads/leads-list.html"
    model = Leads
    context_object_name = "leads"


class ListLeadsSearch(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "leads.view_leads"
    template_name = "leads/leads-list.html"
    model = Leads
    context_object_name = "leads"

    def get_queryset(self) -> QuerySet:
        """Переопределяем метод для поиска клиента по фамилии"""
        query = self.request.GET.get("query")
        return Leads.objects.only(
            "id", "last_name", "first_name", "middle_name"
        ).filter(Q(last_name__iregex=query))

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет идентификатор для отображения сортировки в шаблоне"""
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class DetailLeads(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "leads.view_leads"
    template_name = "leads/leads-detail.html"
    model = Leads


class DeleteLeads(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "leads.delete_leads"
    template_name = "leads/leads-delete.html"
    model = Leads
    success_url = "/leads/"


class UpdateLeads(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "leads.change_leads"
    template_name = "leads/leads-edit.html"
    fields = "first_name", "last_name", "middle_name", "email", "phone"
    model = Leads
    success_url = "/leads/"


class CreateLeads(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "leads.add_leads"
    template_name = "leads/leads-create.html"
    fields = "first_name", "last_name", "middle_name", "email", "phone", "advertising"
    success_url = "/leads/"
    model = Leads

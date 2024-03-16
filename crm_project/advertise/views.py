from typing import Any

from django.core.cache import cache
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Advertise
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Sum, Count, F, QuerySet, Q


class ListAds(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required: str = "advertise.view_advertise"
    template_name: str = "ads/ads-list.html"
    model: Any = Advertise
    context_object_name: str = "ads"


class AdsSearch(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required: str = "advertise.view_advertise"
    template_name: str = "ads/ads-list.html"
    model: Any = Advertise
    context_object_name: str = "ads"

    def get_queryset(self) -> QuerySet:
        """Переопределяем метод для поиска клиента по фамилии"""
        query = self.request.GET.get("query")
        return Advertise.objects.only("id", "name").filter(Q(name__iregex=query))

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет идентификатор для отображения сортировки в шаблоне"""
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class StatisticView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required: str = "advertise.view_advertise"
    template_name: str = "ads/ads-statistic.html"
    model: Any = Advertise
    context_object_name: str = "ads"

    def get_queryset(self) -> QuerySet:
        """
        Переопределяем метод, для получения нужных нам данных, и сортируем по самым доходным
        рекламным кампаниям.
        """
        statistics: QuerySet | Any = cache.get_or_set(
            "statistics",
            Advertise.objects.annotate(
                customers_count=Count("leads__leads__lead_id", distinct=True)
            )
            .annotate(leads_count=Count("leads", distinct=True))
            .annotate(
                profit=Sum("leads__leads__contract__cost", default=0) - F("budget")
            )
            .prefetch_related("leads")
            .prefetch_related("leads__leads")
            .prefetch_related("leads__leads__contract")
            .all()
            .order_by("-profit"),
            60 * 10,
        )
        return statistics


class DetailAds(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required: str = "advertise.view_advertise"
    template_name: str = "ads/ads-detail.html"
    model: Any = Advertise


class DeleteAds(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required: str = "advertise.delete_advertise"
    template_name: str = "ads/ads-delete.html"
    model: Any = Advertise
    success_url: str = "/ads/"


class UpdateAds(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required: str = "advertise.change_advertise"
    template_name: str = "ads/ads-edit.html"
    fields: tuple = "name", "product", "budget"
    model: Any = Advertise
    success_url: str = "/ads/"


class CreateAds(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required: str = "advertise.add_advertise"
    template_name: str = "ads/ads-create.html"
    fields: tuple = "name", "product", "budget"
    success_url: str = "/ads/"
    model: Any = Advertise

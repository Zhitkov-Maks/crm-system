from typing import Any

from django.db.models import Count, QuerySet, Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Products


class ListProducts(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Класс для отображения страницы со списком предоставляемых услуг. Страницу может
    просматривать пользователь у которого есть разрешение 'view_products'.
    """
    permission_required: str = "products.view_products"
    template_name: str = "products/products-list.html"
    model: Any = Products
    context_object_name: str = "products"

    def get_queryset(self) -> QuerySet:
        """
        Переопределяем метод, чтобы сначала показывать услуги которые наиболее пользуются спросом,
        (чем больше заключено контрактов с этой услугой).
        """
        return (
            Products.objects.only("id", "name")
            .annotate(Count("products"))
            .prefetch_related("products")
            .all()
            .order_by("-products__count")
        )


class ProductsSearch(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Класс для отображения страницы со списком найденных по имени предоставляемых услуг.
    Страницу может просматривать пользователь у которого есть разрешение 'view_products'.
    """
    permission_required: str = "products.view_products"
    template_name: str = "products/products-list.html"
    model: Any = Products
    context_object_name: str = "products"

    def get_queryset(self) -> QuerySet:
        """
        Переопределяем метод для поиска услуг по вхождению подстроки в строке с
        названием услуги.
        """
        query: str | None = self.request.GET.get("query")
        return (
            Products.objects.only("id", "name")
            .annotate(Count("products"))
            .prefetch_related("products")
            .filter(Q(name__iregex=query))
            .order_by("-products__count")
        )

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        """
        Добавляет идентификатор для отображения введенного пользователем слова для поиска.
        """
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class DetailProducts(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    Класс для отображения детальной информации о предоставляемой услуге.
    Доступен пользователям у которых есть разрешение 'view_products'.
    """
    permission_required: str = "products.view_products"
    template_name: str = "products/products-detail.html"
    model: Any = Products


class DeleteProducts(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):  # type: ignore
    """
    Класс для отображения страницы удаления услуги.
    Доступен пользователям у которых есть разрешение 'delete_products'.
    Комментарий type: ignore нужен для mypy, который почему-то выдает в данном месте ошибку
    'Definition of "object" in base class "DeletionMixin" is
    incompatible with definition in base class "BaseDetailView"'
    """
    permission_required: str = "products.delete_products"
    template_name: str = "products/products-delete.html"
    model: Any = Products
    success_url: str = "/products/"

    def post(self, request, *args, **kwargs) -> HttpResponse:
        """
        Переопределили метод пост для того чтобы не выпадала 500 ошибка при
        попытке удалить услугу, с которой через кампании связаны потенциальные клиенты.
        Которых я защитил от удаления при удалении услуги.
        """
        product: Products = self.get_object()
        try:
            product.delete()
            return redirect("/products/")
        except ProtectedError:
            return HttpResponse(
                "<h1>Невозможно удалить услугу так как есть связанные записи.</h1>"
            )


class UpdateProducts(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Класс для обновления данных у услуги. Доступен пользователям у
    которых имеется разрешение 'change_products'.
    """
    permission_required: str = "products.change_products"
    template_name: str = "products/products-edit.html"
    fields: tuple = "name", "description", "cost"
    model: Any = Products
    success_url: str = "/products/"


class CreateProducts(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Класс для создания услуги, доступен пользователям с разрешением 'add_products'."""
    permission_required: str = "products.add_products"
    template_name: str = "products/products-create.html"
    fields: tuple = "name", "description", "cost"
    success_url: str = "/products/"
    model: Any = Products

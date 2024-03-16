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
from .models import Products
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ListProducts(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "products.view_products"
    template_name = "products/products-list.html"
    model = Products
    context_object_name = "products"

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
    permission_required = "products.view_products"
    template_name = "products/products-list.html"
    model = Products
    context_object_name = "products"

    def get_queryset(self) -> QuerySet:
        """Переопределяем метод для поиска клиента по фамилии"""
        query = self.request.GET.get("query")
        return (
            Products.objects.only("id", "name")
            .annotate(Count("products"))
            .prefetch_related("products")
            .filter(Q(name__iregex=query))
            .order_by("-products__count")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляет идентификатор для отображения сортировки в шаблоне"""
        context = super().get_context_data()
        key = self.request.GET.get("query")
        context.update({"query": key})
        return context


class DetailProducts(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "products.view_products"
    template_name = "products/products-detail.html"
    model = Products


class DeleteProducts(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "products.delete_products"
    template_name = "products/products-delete.html"
    model = Products
    success_url = "/products/"

    def post(self, request, *args, **kwargs) -> HttpResponse:
        """
        Переопределили метод пост для того чтобы не выпадала 500 ошибка при
        попытке удалить услугу, с которой через кампании связаны потенциальные клиенты.
        Которых я защитил от удаления при удалении услуги.
        """
        product = self.get_object()
        try:
            product.delete()
            return redirect("/products/")
        except ProtectedError:
            return HttpResponse(
                f"<h1>Невозможно удалить услугу так как есть связанные записи.</h1>"
            )


class UpdateProducts(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "products.change_products"
    template_name = "products/products-edit.html"
    fields = "name", "description", "cost"
    model = Products
    success_url = "/products/"


class CreateProducts(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "products.add_products"
    template_name = "products/products-create.html"
    fields = "name", "description", "cost"
    success_url = "/products/"
    model = Products

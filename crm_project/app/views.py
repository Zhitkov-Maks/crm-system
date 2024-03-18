from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, QuerySet
from django.views.generic import TemplateView
from django.core.cache import cache
from products.models import Products
from advertise.models import Advertise
from leads.models import Leads
from customers.models import Customers


class IndexView(LoginRequiredMixin, TemplateView):
    """Класс для отображения главной страницы."""

    template_name: str = "users/index.html"

    def get_context_data(self, **kwargs) -> dict:
        """
        Добавляем в контекст данные для общей статистики.
        Данные кэшируем.
        """
        context = super().get_context_data()
        products_count: QuerySet | Any = cache.get_or_set(
            "products_count", Products.objects.count(), 60 * 10
        )
        advertisements_count: QuerySet | Any = cache.get_or_set(
            "advertisements_count", Advertise.objects.count(), 60 * 10
        )
        leads_count: QuerySet | Any = cache.get_or_set(
            "leads_count", Leads.objects.count(), 60 * 10
        )
        customers_count: QuerySet | Any = cache.get_or_set(
            "customers_count",
            Customers.objects.all().aggregate(count=Count("lead_id", distinct=True)),
            60 * 10,
        )
        context.update(
            {
                "products_count": products_count,
                "advertisements_count": advertisements_count,
                "leads_count": leads_count,
                "customers_count": customers_count.get("count"),
            }
        )
        return context

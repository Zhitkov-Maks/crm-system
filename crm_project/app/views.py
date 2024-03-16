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

    template_name = "users/index.html"

    def get_context_data(self):
        """
        Добавляем в контекст данные для общей статистики.
        Данные кэшируем.
        """
        context = super().get_context_data()
        products_count = cache.get_or_set(
            "products_count", Products.objects.count(), 60 * 30
        )
        advertisements_count = cache.get_or_set(
            "advertisements_count", Advertise.objects.count(), 60 * 30
        )
        leads_count = cache.get_or_set("leads_count", Leads.objects.count(), 60 * 30)
        customers_count = cache.get_or_set(
            "customers_count",
            Customers.objects.all().aggregate(count=Count("lead_id", distinct=True)),
            60 * 30,
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

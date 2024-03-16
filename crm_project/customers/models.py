from django.db import models
from django.db.models import ForeignKey, OneToOneField

from leads.models import Leads
from contracts.models import Contracts


class Customers(models.Model):
    """Модель для представления активных клиентов."""
    lead: ForeignKey = models.ForeignKey(
        Leads, on_delete=models.CASCADE, related_name="leads"
    )
    contract: OneToOneField = models.OneToOneField(
        Contracts, on_delete=models.CASCADE, related_name="contracts"
    )

    def __str__(self):
        return f"{str(self.lead)}"

    class Meta:
        verbose_name = "активный клиент"
        verbose_name_plural = "активные клиенты"
        unique_together = ("lead", "contract")

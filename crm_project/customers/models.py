from django.db import models
from leads.models import Leads


class Customers(models.Model):
    lead = models.ForeignKey(Leads, on_delete=models.CASCADE, related_name='leads')

    def __str__(self):
        return f'{str(self.lead)}'

    class Meta:
        ordering = ('lead',)
        verbose_name = 'активный клиент'
        verbose_name_plural = 'активные клиенты'

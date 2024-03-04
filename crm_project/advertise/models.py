from django.db import models
from products.models import Products


class Advertise(models.Model):
    """Модель для представления рекламных компаний."""
    name = models.CharField(max_length=200, verbose_name='Компания')
    budget = models.DecimalField(verbose_name="Бюджет", max_digits=14, decimal_places=2)
    product = models.ManyToManyField(Products, verbose_name="Услуга", related_name='services')
    promotion_channel = models.CharField(max_length=200, verbose_name='Канал продвижения')

    def __str__(self):
        return f'{str(self.name)}'

    class Meta:
        ordering = ('budget',)
        verbose_name = 'advertise'
        verbose_name_plural = 'advertises'

from django.db import models
from products.models import Products


class Contracts(models.Model):
    """Модель для представления рекламных компаний."""
    name = models.CharField(max_length=200, verbose_name='Название')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Продукт", related_name='products')
    file = models.FileField(upload_to="files/contracts/", default='')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')
    cost = models.DecimalField(verbose_name="Сумма", max_digits=14, decimal_places=2)

    def __str__(self):
        return f'{str(self.name)}'

    class Meta:
        ordering = ('cost',)
        verbose_name = 'контракт'
        verbose_name_plural = 'контракты'

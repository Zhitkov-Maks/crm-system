from django.db import models


class Products(models.Model):
    """Модель для представления услуг."""
    name = models.CharField(max_length=200, verbose_name='Услуга')
    description = models.TextField(max_length=10_000, verbose_name='Описание')
    cost = models.DecimalField(verbose_name="Цена", max_digits=14, decimal_places=2)

    def __str__(self):
        return f'{str(self.name)[:40]}...'

    class Meta:
        ordering = ('name',)
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

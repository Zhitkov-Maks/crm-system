from django.db import models
from django.db.models import CharField, TextField, DecimalField


class Products(models.Model):
    """Модель для представления услуг."""

    name: CharField = models.CharField(max_length=200, verbose_name="Услуга")
    description: TextField = models.TextField(max_length=3000, verbose_name="Описание")
    cost: DecimalField = models.DecimalField(
        verbose_name="Цена", max_digits=14, decimal_places=2
    )

    def __str__(self):
        return f"{str(self.name)}"

    class Meta:
        """Указываем сортировку и имена которые будут указываться в админ панели."""
        ordering = ("name",)
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

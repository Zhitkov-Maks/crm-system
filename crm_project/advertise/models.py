from django.db import models
from django.db.models import CharField, DecimalField, ForeignKey

from products.models import Products


class Advertise(models.Model):
    """Модель для представления рекламных компаний."""

    name: CharField = models.CharField(max_length=300, verbose_name="Кампания")
    budget: DecimalField = models.DecimalField(
        verbose_name="Бюджет", max_digits=14, decimal_places=2
    )
    product: ForeignKey = models.ForeignKey(
        Products,
        verbose_name="Услуга",
        related_name="services",
        on_delete=models.CASCADE,
    )
    promotion_channel: CharField = models.CharField(
        max_length=200, verbose_name="Канал продвижения"
    )

    def __str__(self):
        return f"{str(self.name)}"

    class Meta:
        """
        Указываем как будут сортироваться рекламные кампании и
        как будет показываться название в админ панели.
        """
        ordering: tuple = ("name",)
        verbose_name: str = "кампания"
        verbose_name_plural: str = "кампании"

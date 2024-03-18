from django.db import models
from django.core.validators import RegexValidator
from django.db.models import ForeignKey, CharField, EmailField

from advertise.models import Advertise


class Leads(models.Model):
    """Модель для представления рекламных клиентов."""

    last_name: CharField = models.CharField(max_length=200, verbose_name="Фамилия")
    first_name: CharField = models.CharField(max_length=200, verbose_name="Имя")
    middle_name: CharField = models.CharField(max_length=200, verbose_name="Отчество")
    phone_regex: RegexValidator = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Некорректный ввод. формат: '+999999999' от 9 до 15 цифр.",
    )
    phone: CharField = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )
    email: EmailField = models.EmailField(max_length=50, verbose_name="Email")
    advertising: ForeignKey = models.ForeignKey(
        Advertise,
        null=True,
        verbose_name="кампания",
        on_delete=models.SET_NULL,
        related_name="leads",
    )

    def __str__(self):
        return f"{str(self.last_name)} {str(self.first_name)} {str(self.middle_name)} "

    class Meta:
        """Указываем сортировку и имена которые будут указываться в админ панели."""

        ordering: tuple = ("last_name",)
        verbose_name: str = "потенциальный клиент"
        verbose_name_plural: str = "потенциальные клиенты"
        unique_together: tuple = ("last_name", "first_name", "middle_name", "email", "phone")

from django.db import models
from django.core.validators import RegexValidator


class Leads(models.Model):
    """Модель для представления рекламных клиентов."""
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=50, verbose_name='Email')

    def __str__(self):
        return f'{str(self.last_name)} {str(self.first_name)}'

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'потенциальный клиент'
        verbose_name_plural = 'потенциальные клиенты'

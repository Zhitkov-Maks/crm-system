from django import forms

from .models import Contracts


class ContractForm(forms.ModelForm):
    """Форма для создания контрактов."""
    class Meta:
        """
        Указываем какая модель будет использоваться для формы,
        какие поля, и некоторые настройки отображения.
        """
        model = Contracts
        fields = "__all__"
        help_texts = {
            "product": "Выберите услугу",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Название контракта"}),
            "start_date": forms.SelectDateWidget(attrs={"format": "%Y/%m/%d"}),
            "end_date": forms.SelectDateWidget(attrs={"format": "%Y/%m/%d"}),
            "cost": forms.NumberInput(attrs={"placeholder": "Сумма контракта"}),
        }

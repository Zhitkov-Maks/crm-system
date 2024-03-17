from django import forms
from .models import Customers


class CustomerForm(forms.ModelForm):
    """Форма для создания активного клиента."""
    class Meta:
        """Указываем модель которая, будет использоваться для формы и
        какие поля будут отображаться."""
        model = Customers
        fields = "__all__"
        widgets = {
            "lead": forms.Select(),
            "contract": forms.Select(),
        }

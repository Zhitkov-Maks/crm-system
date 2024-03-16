from django import forms
from .models import Customers


class CustomerForm(forms.ModelForm):
    """Форма для создания активного клиента."""
    class Meta:
        model = Customers
        fields = "__all__"
        widgets = {
            "lead": forms.Select(),
            "contract": forms.Select(),
        }

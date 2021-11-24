from django.forms import ModelForm
from django.forms.widgets import NumberInput

from sistema_venta.models import Boleto

class BoletoForm(ModelForm):
    class Meta:
        model = Boleto
        fields = '__all__'
        widgets = {
            'precio': NumberInput(attrs={'type':'precio'})
        }

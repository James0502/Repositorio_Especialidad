from django import forms
from .models import Cotizacion

class CotizacionForm(forms.ModelForm):
    class Meta: 
        model = Cotizacion
        fields = '__all__'

from django import forms

from .models import Prestamo

# Formulario mapeando el modelo Prestamo
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro',
        )
from django import forms
from applications.libro.models import Libro
from .models import Prestamo

# Formulario mapeando el modelo Prestamo
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro',
        )

class MultiplePrestamoForm(forms.ModelForm):

    #especificar que tipo de formulario queremos que se construya
    libros = forms.ModelMultipleChoiceField(
        #se necesita saber qué conjunto de datos se va cargar 
        #queryset = Libro.objects.all()
        queryset = None,
        #campo requerido obligatoriamente
        required = True,
        #cómo queremos que se muestre este campo
        widget = forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Prestamo
        fields = (
            'lector',
        )

    #Función con la que se pueden inicializar valores en el formulario
    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        #inicializamos el atributo queryset de libros
        self.fields['libros'].queryset = Libro.objects.all()
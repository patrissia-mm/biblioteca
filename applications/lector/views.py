from datetime import date

from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Prestamo

#importación de formulario
from .forms import PrestamoForm

# Create your views here.
# Vista para registrar un Prestamo
class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    #Sobreescribiendo la función form_valid() del FormView para hacer validaciones propias
    def form_valid(self, form):
        #Método create para guardar datos:
        #  Prestamo.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fecha_prestamo = date.today(),
        #     devuelto = False
        # ) 

        # Método save para guardar datos:
        prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False
        )
        prestamo.save()
        
        return super(RegistrarPrestamo, self).form_valid(form)
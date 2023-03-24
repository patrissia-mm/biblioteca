from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from .models import Prestamo

#importación de formulario
from .forms import PrestamoForm, MultiplePrestamoForm

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

        #Procedimiento para descontar el stock después de un préstamo desde las vistas, puede hacerse tb en los modelos
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock - 1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)
    
#Nueva vista para registrar préstamo con otras formas de validación
class AddPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults = {
                'fecha_prestamo':date.today()
            }
        )

        #En caso de no haber creado el registro redireccionar a otra página
        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')
        
# Ejemplo de vista para registrar varios libros en un préstamo
class AddMultiplePrestamo(FormView):
    template_name = 'lector/add_multiple_prestamo.html'
    form_class = MultiplePrestamoForm
    success_url = '.'

    def form_valid(self, form):
        #prueba de lo que nos está enviando el formulario
        # print(form.cleaned_data['lector'])
        # print(form.cleaned_data['libros'])
        prestamos = []
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = l,
                fecha_prestamo = date.today(),
                devuelto = False
            )
            prestamos.append(prestamo)
        #Enviamos la lista de objectos prestamo para guardar
        Prestamo.objects.bulk_create(
            prestamos
        )

        return super(AddMultiplePrestamo, self).form_valid(form)
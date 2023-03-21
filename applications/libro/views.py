from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Libro

# Create your views here.
class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        f1 = self.request.GET.get('fecha1','') 
        f2 = self.request.GET.get('fecha2','')
        if f1 and f2:
            return Libro.objects.filtrar_libros2(palabra_clave, f1, f2)
        else:
            return Libro.objects.filtrar_libros(palabra_clave)

class ListLibrosTgm(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        return Libro.objects.filtrar_libros_tgm(palabra_clave)

class ListLibrosCategoria(ListView):
    context_object_name = 'lista_libros_cat'
    template_name = 'libro/lista2.html'

    def get_queryset(self):
        return Libro.objects.listar_libros_categoria(3)

class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"



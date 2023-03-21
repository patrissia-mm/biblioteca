from django.shortcuts import render
from django.views.generic import ListView

#modelos locales
from .models import Autor

# Create your views here.
"""class ListAutores(ListView):
    #model=Autor
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        return Autor.objects.listar_autores()"""

class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = "autor/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        return Autor.objects.buscar_autor4(palabra_clave)


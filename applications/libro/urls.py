from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(
        'libros/', 
        views.ListLibros.as_view(), 
        name='libros'
    ),

    path(
        'libros-tgm/', 
        views.ListLibrosTgm.as_view(), 
        name='libros-tgm'
    ),

    path(
        'libros-categoria/', 
        views.ListLibrosCategoria.as_view(), 
        name='libros2'
    ),

    path(
        'libro-detalle/<pk>/', 
        views.LibroDetailView.as_view(), 
        name='libro-detalle'
    ),
]
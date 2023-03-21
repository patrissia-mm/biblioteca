import datetime
from django.db import models
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity


class LibroManager(models.Manager):
    def filtrar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains = kword
        )
        return resultado

    def filtrar_libros_tgm(self, kword):
        if kword:
            resultado = self.filter(
                titulo__trigram_similar = kword
            )
            return resultado
        else:
            return self.all()[:10]
    
    def filtrar_libros2(self, kword, fecha1, fecha2):
        #convirtiendo fecha a formatos correctos para algunos navegadores
        f1=datetime.datetime.strptime(fecha1,"%Y-%m-%d")
        f2=datetime.datetime.strptime(fecha2,"%Y-%m-%d")

        resultado = self.filter(
            titulo__icontains = kword,
            fecha__range = (f1, f2)
        )
        return resultado

    def listar_libros_categoria(self, categoria):
        resultado = self.filter(
            categoria__id = categoria
        ).order_by('titulo')
        return resultado

    #Añadir un autor a los autores de un libro (el autor debe estar ya registrado en la tabla de autores)
    def add_autor_libro(self, id_libro, autor):
        libro = self.get(id = id_libro)
        libro.autores.add(autor)
        #para eliminar sería libro.autores.remove(autor)
        return libro

    #Contar la cantidad de préstamos de un libro -->> AGGREGATE
    def libro_num_prestamos(self):
        resultado=self.aggregate(
            num_prestamos = Count('libro_prestamo')
        )
        return resultado

    #Prueba contar cantidad de veces que ha sido prestado cada libro.
    def num_libros_prestados(self):
        #EL ANNOTATE REQUIERE UN PARÁMETRO PARA AGRUPAR...
        resultado = self.annotate(
            num_prestados = Count('libro_prestamo')
        )
        for r in resultado:
            print('******')
            print(r, r.num_prestados)
        
        return resultado

class CategoriaManager(models.Manager):
    def categorias_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id = autor
        ).distinct()

    #Contar la cantidad de libros de cada categoría -->> ANNOTATE
    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )

        for r in resultado:
            print(r, r.num_libros)

        return resultado
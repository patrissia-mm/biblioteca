from django.db import models
from django.db.models import Count, Avg, Sum
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):
    
    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id = '1'
        ).aggregate(
            promedido_edad = Avg('lector__edad'),
            suma_edades = Sum('lector__edad')
        )
        return resultado

    #Cantidad de veces que se ha prestado cada libro, el resultado es un diccionario debido a 'values'
    def num_libros_prestados(self):
        resultado = self.values(
            #agrupar por libro
            'libro'
            #,'lector'
        ).annotate(
            num_prestados = Count('libro'),
            titulo = Lower('libro__titulo')
        )
        for r in resultado:
            print('******')
            print(r, r['num_prestados'])
        
        return resultado
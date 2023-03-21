from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):
    """ Managers para el modelo autor """
    """def listar_autores(self):
        return self.all()"""
    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains = kword
        )
        return resultado

    def buscar_autor2(self, kword):
        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)
        )
        return resultado
    
    #def buscar_autor3(self, kword):
    #resultado = self.filter(
    #nombre__icontains = kword
    #).exclude(
    #    Q(edad__icontains = 35) | Q(edad__icontains = 65)
    #) """

    def buscar_autor3(self, kword):
        resultado = self.filter(
            Q(nombre__icontains = kword) | Q(apellidos__icontains = kword)
        ).filter(
            Q(edad__icontains = 120) | Q(edad__icontains = 110)
        )
        return resultado
    
    def buscar_autor4(self, kword):
        resultado = self.filter(
            edad__gt = 100,
            edad__lt = 120
        ).order_by('apellidos', 'nombre', 'id')
        return resultado

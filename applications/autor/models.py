from django.db import models

#managers
from .managers import AutorManager

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(
        max_length = 50
    )

    apellidos = models.CharField(
        max_length = 50
    )

    nacionalidad = models.CharField(
        max_length = 30
    )

    edad = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre + '-' + self.apellidos
    
    class Meta:
        abstract = True

class Autor(Persona):
    pseudonimo = models.CharField(
        'pseudonimo',
        max_length=30,
        blank=True
    )
    objects = AutorManager()    


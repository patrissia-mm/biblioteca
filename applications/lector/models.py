from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

from applications.libro.models import Libro
from applications.autor.models import Persona
from .managers import PrestamoManager

class Lector(Persona):
   class Meta:
       verbose_name = 'Lector'
       verbose_name_plural = 'Lectores'

class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE
    )

    libro = models.ForeignKey(
        Libro,
        on_delete = models.CASCADE,
        related_name='libro_prestamo'
    )

    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(
        blank = True,
        null = True
    )

    devuelto = models.BooleanField()

    objects = PrestamoManager()

    #Sobre escribiend un método para descontar el stock después de un préstamo desde los modelos, puede hacerse tb en las vistas
    def save(self, *args, **kwargs):
        self.libro.stock = self.libro.stock -1
        self.libro.save()
        super(Prestamo, self).save(*args, **kwargs)

    def __str__(self):
        return self.libro.titulo

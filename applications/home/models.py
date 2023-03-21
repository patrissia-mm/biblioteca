from django.db import models

# Create your models here.
class Persona(models.Model):
    """Model definition for MODELNAME."""
    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)
    
    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        # modificar el nombre por defecto de la tabla
        db_table = 'persona'
        # que 1 pais y 1 edad sólo pueda registrarse 1 sola vez
        unique_together = ['pais', 'edad']
        # que la edad registrada sea mayor a 18 años
        constraints =[
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]
        abstract = True

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.full_name
    
class Empleado(Persona):
    puesto = models.CharField('Puesto', max_length=25)

class Cliente(Persona):
    email = models.EmailField('Email')

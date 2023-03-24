from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.signals import post_save

#Importaciones de terceros
from PIL import Image

from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager



# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(
        max_length = 30
    )
    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete = models.CASCADE,
        related_name='categoria_libro'
    )

    autores = models.ManyToManyField(
        Autor
    )

    titulo = models.CharField(
        max_length = 50
    )

    fecha = models.DateField('Fecha de lanzamiento')

    portada = models.ImageField(upload_to='portada')

    vistas = models.PositiveIntegerField()

    stock = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return str(self.id) + "-" +self.titulo

# para indicar a la ORM que esta función trababjará como un SIGNAL se le deben pasar ciertos parámetros
# sender: hace referencia hacia donde se va ejecutar la función
# instance: la instancia que se está trabajando en ese momento
# **kwargs: diccionario que generalmente se pasa al usar la ORM de Django
def optimize_image(sender, instance, **kwargs):
    # print("======================")
    # print(instance)
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality = 20,  optimize=True)

post_save.connect(optimize_image, sender=Libro)
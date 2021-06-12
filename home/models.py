from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=250)
    contenido = RichTextUploadingField()

    def __str__(self):
        return '%s' % self.titulo

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    mensaje = models.TextField()
    fecha = models.DateField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.nombre

class RedesSociales(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    link = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return '%s' % self.nombre

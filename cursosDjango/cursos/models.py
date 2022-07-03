from django.db import models

# Create your models here.

class Cursos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Id curso")
    nombre = models.TextField()
    mensaje = models.TextField()
    imagen = models.ImageField(null=True,upload_to="fotos")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre

class MensajeUsuario(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="ID Usuario")
    nombre = models.TextField()
    email = models.EmailField()
    curso = models.TextField()
    telefono = models.IntegerField()
    mensaje = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje usuario"
        verbose_name_plural = "Mensajes usuarios"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
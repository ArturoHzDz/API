from django.db import models

# Create your models here.
class Project(models.Model):
    Título = models.CharField(max_length=200)
    Contenido = models.TextField()
    Autor = models.CharField(max_length=200)
    Creado = models.DateTimeField(auto_now_add=True)
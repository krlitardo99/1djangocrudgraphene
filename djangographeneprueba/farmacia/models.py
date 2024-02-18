from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add = 'true')

    def __str__(self):
        return self.nombre


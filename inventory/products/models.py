from django.db import models

class Product(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.
class Prestamo(models.Model):
    id_prestamo = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_devolucion = models.DateField()
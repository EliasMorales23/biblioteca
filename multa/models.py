from django.db import models

# Create your models here.
class Multa(models.Model):
    id_multa = models.IntegerField(primary_key=True)
    fecha_multa = models.DateField()
    fecha_pago = models.DateField()
    
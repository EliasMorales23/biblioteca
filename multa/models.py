from django.db import models

# Create your models here.
class Multa(models.Model):
    id_multa = models.IntegerField(primary_key=True)
    nombre = models.CharField( null=True,
        blank=True)
    fecha_multa = models.DateField()
    fecha_pago = models.DateField(
        null=True,
        blank=True
        )
    monto = models.IntegerField(null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre


    
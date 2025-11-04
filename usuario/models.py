from django.db import models
from multa import models as multa_models
# Create your models here.
class Usuario(models.Model):
    numero_socio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    id_multa = models.ForeignKey(multa_models.Multa)
    
    
    
    
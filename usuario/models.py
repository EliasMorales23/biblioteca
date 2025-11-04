from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    numero_socio = models.IntegerField(primary_key=True)
    
    
    
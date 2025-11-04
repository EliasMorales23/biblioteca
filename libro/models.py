from django.db import  models
from prestamo import models as prestamo_models
from usuario import models as usuario_models
# Create your models here.
class Libro(models.Model):
    isbn = models.IntegerField(primary_key=True)
    autor = models.CharField()
    titulo = models.CharField(max_length=30)
    estado = models.BooleanField()
    id_prestamo = models.ForeignKey(prestamo_models.Prestamo)
    numero_socio = models.ForeignKey(usuario_models.Usuario)
    
    
    
    
    
    
    
    
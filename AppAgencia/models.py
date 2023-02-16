from django.db import models

# Create your models here.
class Proyecto(models.Model):
    cliente = models.CharField(max_length=100)
    campaña = models.CharField(max_length=100)
    deadline = models.DateField
    codigo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.cliente
    
    def __str__(self):
        return self.campaña
    
    def __str__(self):
        return self.deadline
    
    def __str__(self):
        return self.codigo
    
class Recursos(models.Model):
    teamleader = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    id_proyecto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.teamleader
    
    def __str__(self):
        return self.equipo
    
    def __str__(self):
        return self.id_proyecto

class Estado(models.Model):
    id_proyecto = models.CharField(max_length=100)
    comentarios = models.CharField(max_length=500)
    finalizado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.id_proyecto
    
    def __str__(self):
        return self.comentarios

from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    origen = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.marca}"
    
class Partner(models.Model):
    nombre = models.CharField(max_length=50)
    antiguedad = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
class Oferta(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descuentoEspecial = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} ({self.descuentoEspecial})"
    
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    nombreAlumno = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} ({self.comision})"
    
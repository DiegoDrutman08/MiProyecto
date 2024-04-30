from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre

class Comision(models.Model):
    nombre = models.PositiveIntegerField(unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)    
    estudiante = models.ManyToManyField(Estudiante)
 
    def __str__(self):
        return str(self.nombre)
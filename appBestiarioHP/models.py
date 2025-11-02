from django.db import models

class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()  # Breve descripción de la raza

    def __str__(self):
        return self.nombre

class Peligro(models.Model):
    nombre = models.CharField(max_length=50)  # X, XX, XXX, etc.
    descripcion = models.TextField()          # Breve descripción del nivel de peligro

    def __str__(self):
        return self.nombre

class Criatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()  # Descripción general de la criatura
    donde_se_encuentra = models.CharField(max_length=200)  # Lugar donde suele encontrarse
    caracteristicas = models.JSONField(blank=True, null=True)  # Lista de características
    raza = models.ManyToManyField(Raza, blank=True)  # Una criatura puede pertenecer a varias razas
    categoria_peligro = models.ForeignKey(Peligro, on_delete=models.CASCADE)  # Categoría de peligro

    def __str__(self):
        return self.nombre

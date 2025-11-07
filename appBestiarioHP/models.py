from django.db import models

class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()  # Descripcion de la raza

    def __str__(self):
        return self.nombre

class Peligro(models.Model):
    nombre = models.CharField(max_length=50)  # X, XX, XXX, etc.
    descripcion = models.TextField()          # Descripcion del nivel de peligro

    def __str__(self):
        return self.nombre

class Criatura(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()  # Descripcion general de la criatura
    donde_se_encuentra = models.CharField(max_length=200)  # Donde suele encontrarse
    caracteristicas = models.JSONField(blank=True, null=True)  # Caracteristicas principales
    raza = models.ManyToManyField(Raza, blank=True)  # Debido a que una criatura no puede pertenecer a mas de una categoria de peligro, hemos decidido que pueda pertenecer a dos razas, por ejemplo, reptil y volador
    categoria_peligro = models.ForeignKey(Peligro, on_delete=models.CASCADE)  # Categoría de peligro

    def __str__(self):
        return self.nombre

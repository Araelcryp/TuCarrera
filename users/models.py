from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=50)
    curp = models.CharField(max_length=18)
    municipio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    bachillerato = models.CharField(max_length=50)
    matricula = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.username} Profile'

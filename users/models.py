from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    curp = models.CharField(max_length=18)
    procedencia = models.CharField(max_length=10, choices=[('si', 'Sí'), ('no', 'No')], default='no')
    estado = models.CharField(max_length=50, null=True, blank=True)  # Solo si la preparatoria es fuera de Querétaro
    institucion = models.CharField(max_length=100, null=True, blank=True)  # Solo si la preparatoria es fuera de Querétaro
    municipio = models.CharField(max_length=50, null=True, blank=True)  # Si la preparatoria es en Querétaro
    bachillerato = models.CharField(max_length=100, null=True, blank=True)  # Incluir opción de "otro"
    otro_bachillerato = models.CharField(max_length=100, null=True, blank=True)  # Campo opcional si elige "otro"
    matricula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    
    # Progreso individual por sección Primer Paso
    progreso_personalidad = models.IntegerField(default=0)
    progreso_autoestima = models.IntegerField(default=0)
    progreso_valores = models.IntegerField(default=0)
    progreso_logros = models.IntegerField(default=0)
    progreso_inteligencias = models.IntegerField(default=0)
    progreso_testInteligencias = models.IntegerField(default=0)
    
    # Progreso individual por sección Segundo Paso
    progreso_presentacionsegundopaso = models.IntegerField(default=0)
    progreso_testsegundopaso = models.IntegerField(default=0)
    
    # Progreso individual por sección Tercer Paso
    
    
    def __str__(self):
        return f'{self.user.username} Profile'

import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import timedelta, timezone

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
    telefono = models.CharField(max_length=30)
    email_tutor = models.EmailField(null=True, blank=True)
    
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
    progreso_infografiatercerpaso = models.IntegerField(default=0)
    # Tercer Paso sección 2
    progreso_tablerotercerpaso = models.IntegerField(default=0)
    progreso_videotercerpaso = models.IntegerField(default=0)
    progreso_videoconsejotercerpaso = models.IntegerField(default=0)
    progreso_presentaciontercerpaso = models.IntegerField(default=0)
    
    # Progreso individual por sección Cuarto Paso
    progreso_tablerocuartopaso = models.IntegerField(default=0)
    progreso_videocuartopaso = models.IntegerField(default=0)
    progreso_agendacuartopaso = models.IntegerField(default=0)
    
    # Progreso individual por sección Quinto Paso
    progreso_imagenquintopaso = models.IntegerField(default=0)
    progreso_tableroquintopaso = models.IntegerField(default=0)
    progreso_infografiaquintopaso = models.IntegerField(default=0)
    
    # Progreso individual por sección Sexto Paso
    progreso_tablerosextopaso = models.IntegerField(default=0)
    
    # Progreso individual por sección Septimo Paso
    progreso_fraseseptimopaso = models.IntegerField(default=0)
    progreso_imagenseptimopaso = models.IntegerField(default=0)
    progreso_imagen2septimopaso = models.IntegerField(default=0)
    progreso_formatoseptimopaso = models.IntegerField(default=0)
    # Septimo Paso sección 2
    progreso_infografiaseptimopaso = models.IntegerField(default=0)
    progreso_formato2septimopaso = models.IntegerField(default=0)
    
    def tiempo_total_en_plataforma(self):
        tiempo_transcurrido = timedelta.total_seconds((timezone.now() - self.user.date_joined)) / 3600  # Convertir a horas
        return round(tiempo_transcurrido, 1)  # Redondear a una decimal
    
    def __str__(self):
        return f'{self.user.username} Profile'

class Meta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    descripcion = models.CharField(max_length=255)
    fecha_objetivo = models.DateField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descripcion} - {self.user.username}"
    
def constancia_upload_path(instance, filename):
    """
    Función para definir la ruta de almacenamiento de la constancia
    dependiendo del bachillerato del usuario.
    """
    if instance.user.profile.procedencia == 'si':  # Estudió en Querétaro
        path = os.path.join("constancias", instance.user.profile.municipio or "Desconocido", instance.user.profile.bachillerato or "Sin_Bachillerato")
    elif instance.user.profile.procedencia == 'no':  # Estudió fuera de Querétaro
        path = os.path.join("constancias", instance.user.profile.estado or "Desconocido", instance.user.profile.institucion or "Sin_Institucion")
    elif instance.user.profile.otro_bachillerato:  # Eligió "otro"
        path = os.path.join("constancias", "Otras", instance.user.profile.otro_bachillerato)
    else:
        path = os.path.join("constancias", "Otras")
    
    return os.path.join(path, filename.replace(" ", "_"))

class Constancia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    bachillerato = models.CharField(max_length=100)  
    archivo = models.FileField(upload_to=constancia_upload_path)  # Se usa la función para definir la ruta
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    enviado = models.BooleanField(default=False)  

    def __str__(self):
        return f"Constancia de {self.user.username} - {self.bachillerato}"
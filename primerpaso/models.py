from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TestResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="test_result")
    inteligencia_verbal = models.IntegerField(default=0)
    inteligencia_logica = models.IntegerField(default=0)
    inteligencia_visual = models.IntegerField(default=0)
    inteligencia_corporal = models.IntegerField(default=0)
    inteligencia_musical = models.IntegerField(default=0)
    inteligencia_intrapersonal = models.IntegerField(default=0)
    inteligencia_interpersonal = models.IntegerField(default=0)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"Resultados de {self.user.username}"
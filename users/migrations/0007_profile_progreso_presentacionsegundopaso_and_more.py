# Generated by Django 5.0.2 on 2025-03-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_progreso_inteligencias_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='progreso_presentacionSegundoPaso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='progreso_testSegundoPaso',
            field=models.IntegerField(default=0),
        ),
    ]

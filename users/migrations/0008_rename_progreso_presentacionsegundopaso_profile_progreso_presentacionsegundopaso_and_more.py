# Generated by Django 5.0.2 on 2025-03-02 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_progreso_presentacionsegundopaso_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='progreso_presentacionSegundoPaso',
            new_name='progreso_presentacionsegundopaso',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='progreso_testSegundoPaso',
            new_name='progreso_testsegundopaso',
        ),
    ]

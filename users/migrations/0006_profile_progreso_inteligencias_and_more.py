# Generated by Django 5.0.2 on 2025-03-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_progreso_profile_progreso_autoestima_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='progreso_inteligencias',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='progreso_testInteligencias',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.6 on 2024-09-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_progreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='localidad',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lugar_nacimiento',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='progreso',
        ),
        migrations.AddField(
            model_name='profile',
            name='estado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='institucion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='otro_bachillerato',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='procedencia',
            field=models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='no', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bachillerato',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='municipio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

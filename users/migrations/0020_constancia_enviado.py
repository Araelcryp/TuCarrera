# Generated by Django 5.1.2 on 2025-03-03 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_profile_email_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='constancia',
            name='enviado',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.0.3 on 2025-01-09 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_tasks_machine'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name': 'Registro de serviço', 'verbose_name_plural': 'Registro de serviços'},
        ),
    ]

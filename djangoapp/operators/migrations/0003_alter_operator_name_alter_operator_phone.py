# Generated by Django 5.0.3 on 2025-01-08 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0002_alter_operator_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='operator',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Telefone'),
        ),
    ]

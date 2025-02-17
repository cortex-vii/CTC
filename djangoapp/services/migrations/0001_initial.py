# Generated by Django 5.0.3 on 2025-01-08 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('machines', '0001_initial'),
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operators.operator')),
            ],
        ),
    ]

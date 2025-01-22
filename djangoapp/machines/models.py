from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    status = models.CharField(
        max_length=50, 
        choices=[('Active', 'Ativo'), ('Inactive', 'Inativo')], 
        verbose_name='Status'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Máquina"
        verbose_name_plural = "Máquinas"

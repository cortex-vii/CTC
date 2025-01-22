from django.db import models

class Operator(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    phone = models.CharField(max_length=15, verbose_name='Telefone')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Operador"
        verbose_name_plural = "Operadores"

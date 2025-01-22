from django.db import models

class CategoryExit(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria de Saída"
        verbose_name_plural = "Categorias de Saída"
        

class CategoryEntry(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria de Entrada"
        verbose_name_plural = "Categorias de Entrada"

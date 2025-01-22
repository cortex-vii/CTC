from django.db import models
from services.models import Service
from machines.models import Machine
from operators.models import Operator
from categories.models import CategoryEntry  # Importe a Categoria de Entrada

class Entry(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Serviço')
    category = models.ForeignKey(CategoryEntry, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoria de Entrada')
    
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Máquina')
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Operador')
    
    quantity = models.IntegerField(verbose_name='Quantidade')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Unitário', default=0)  # Adiciona um valor padrão
    total_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor Total')  # Valor total (quantity * price)
    
    description = models.TextField(verbose_name='Descrição')
    entry_date = models.DateTimeField(verbose_name='Data de Entrada')

    def __str__(self):
        return f"Entrada para {self.service.client}"

    def save(self, *args, **kwargs):
        # Calcula o valor total com base na quantidade e preço unitário
        if self.quantity and self.price is not None:
            self.total_value = self.quantity * self.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

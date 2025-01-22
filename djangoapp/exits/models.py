from django.db import models
from services.models import Service
from machines.models import Machine
from operators.models import Operator
from categories.models import CategoryExit

class Exit(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Serviço')
    category = models.ForeignKey(CategoryExit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoria de Saída')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Máquina')  # Agora não é obrigatório
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Operador')  # Agora não é obrigatório
    
    quantity = models.IntegerField(verbose_name='Quantidade')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Unitário', default=0)  # Adiciona um valor padrão
    total_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor Total')  # Valor total (quantity * price)
    
    description = models.TextField(verbose_name='Descrição')
    exit_date = models.DateTimeField(verbose_name='Data de Saída')

    def __str__(self):
        return f"Saída para {self.service.client}"

    def save(self, *args, **kwargs):
        # Calcula o valor total com base na quantidade e preço unitário
        if self.quantity and self.price is not None:
            self.total_value = self.quantity * self.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"

from django.db import models
from math import floor

from operators.models import Operator
from services.models import Service
from machines.models import Machine


class Tasks(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, verbose_name='Operador')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Serviço')
    service_date = models.DateField(null=True, blank=True, verbose_name='Data do Serviço')
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Máquina')
    horimeter_end = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Leitura Final do Horímetro (Horas)')
    horimeter_start = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Leitura Inicial do Horímetro (Horas)')
    hours_worked = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True, verbose_name='Horas Trabalhadas')
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor da Hora')
    total_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor Total', editable=False)
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    def __str__(self):
        return f"{self.operator.name} - {self.service.client} (De {self.horimeter_start} a {self.horimeter_end} horas)"

    def save(self, *args, **kwargs):
        # Verifica se as leituras do horímetro são válidas
        if self.horimeter_start is not None and self.horimeter_end is not None:
            if self.horimeter_end >= self.horimeter_start:
                total_hours = self.horimeter_end - self.horimeter_start
                self.hours_worked = total_hours  # Representa as horas reais
            else:
                raise ValueError("O valor de 'horimeter_end' deve ser maior ou igual ao de 'horimeter_start'.")

        # Calcula o valor total
        if self.hours_worked is not None and self.hourly_rate is not None:
            self.total_value = self.hours_worked * self.hourly_rate
        else:
            self.total_value = None

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Registro de serviço"
        verbose_name_plural = "Registro de serviços"

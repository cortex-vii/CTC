from django.db import models
from math import floor

from operators.models import Operator
from services.models import Service
from machines.models import Machine


class Tasks(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, verbose_name='Operador')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Serviço')
    service_date = models.DateField(null=True, blank=True, verbose_name='Data do Serviço')
    machine = models.ForeignKey(Machine, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Máquina')  # Máquina não obrigatória
    horimeter_end = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Leitura Final do Horímetro (Horas)')
    horimeter_start = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Leitura Inicial do Horímetro (Horas)')
    hours_worked = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True, verbose_name='Horas Trabalhadas')
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor da Hora')  # Valor da hora
    total_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor Total', editable=False)  # Valor total calculado
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    def __str__(self):
        return f"{self.operator.name} - {self.service.client} (De {self.horimeter_start} a {self.horimeter_end} horas)"

    def save(self, *args, **kwargs):
        # Calcula as horas trabalhadas em formato de horas e minutos
        if self.horimeter_start is not None and self.horimeter_end is not None:
            total_hours = self.horimeter_end - self.horimeter_start
            if total_hours >= 0:
                hours = floor(total_hours)  # Parte inteira das horas
                minutes = (total_hours - hours) * 60  # Converte a parte decimal para minutos
                self.hours_worked = hours + round(minutes / 100, 2)  # Representa os minutos como fração de 100 (ex.: 1,3)

        # Calcula o valor total
        if self.hours_worked is not None and self.hourly_rate is not None:
            self.total_value = self.hours_worked * self.hourly_rate

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Registro de serviço"
        verbose_name_plural = "Registro de serviços"

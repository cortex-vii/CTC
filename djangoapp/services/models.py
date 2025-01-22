from django.db import models
from machines.models import Machine
from operators.models import Operator

class Service(models.Model):
    client = models.CharField(max_length=100, verbose_name='Cliente')
    description = models.TextField(verbose_name='Descrição')
    machines = models.ManyToManyField(Machine, verbose_name='Máquinas')
    operators = models.ManyToManyField(Operator, verbose_name='Operadores')
    start_date = models.DateTimeField(verbose_name='Data de Início', blank=True, null=True)  # Tornando opcional
    end_date = models.DateTimeField(verbose_name='Data de Término', blank=True, null=True)  # Tornando opcional
    status = models.CharField(
        max_length=50, 
        choices=[('To Do', 'Fazer'), ('In Progress', 'Em progresso'), ('Done', 'Finalizado')],
        verbose_name='Status'
    )

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

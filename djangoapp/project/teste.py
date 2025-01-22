from django.db import models

# Machines Table
class Machine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return self.name

# Operators Table
class Operator(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Services Table
class Service(models.Model):
    client = models.CharField(max_length=100)
    description = models.TextField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Pode ter mais de uma máquina
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)  # Pode ter mais de um operador
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return self.name

# Entries Table
class Entry(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryEntry', on_delete=models.SET_NULL, null=True, blank=True)  # Relacionamento com a categoria de entrada 
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Apenas 1, não precisa ser obrigatório
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)  # Apenas 1, não precisa ser obrigatório
    quantity = models.IntegerField()
    description = models.TextField()
    entry_date = models.DateTimeField()

    def __str__(self):
        return f"Entry for {self.service.name}"

# Exits Table
class Exit(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryExit', on_delete=models.SET_NULL, null=True, blank=True)  # Relacionamento com a categoria de saída
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)  # Apenas 1, não precisa ser obrigatório
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)  # Apenas 1, não precisa ser obrigatório
    quantity = models.IntegerField()
    description = models.TextField()
    exit_date = models.DateTimeField()

    def __str__(self):
        return f"Exit for {self.service.name}"

# Category for Exits
class CategoryExit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Category for Entries
class CategoryEntry(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Tasks (para registrar as horas trabalhadas)
class Tasks(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    horimeter_start = models.DecimalField(max_digits=6, decimal_places=1)  # Leitura inicial do horímetro (em horas)
    horimeter_end = models.DecimalField(max_digits=6, decimal_places=1)  # Leitura final do horímetro (em horas)
    hours_worked = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)  # Horas trabalhadas (calculadas automaticamente)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.operator.name} - {self.service.name} (from {self.horimeter_start} to {self.horimeter_end} hours)"

    def save(self, *args, **kwargs):
        # Calcula a quantidade de horas trabalhadas com base no horímetro
        if self.horimeter_end is not None and self.horimeter_start is not None:
            self.hours_worked = self.horimeter_end - self.horimeter_start  # Subtrai a leitura final pela leitura inicial
        super().save(*args, **kwargs)

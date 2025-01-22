from django.contrib import admin
from .models import Tasks


from rangefilter.filters import (
    DateRangeFilterBuilder,
)


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('operator', 'service', 'formatted_hours_worked', 'formatted_total_value', 'horimeter_end', 'horimeter_start')
    search_fields = ('operator__name', 'service__client', 'description')
    list_filter = ('service',  ('service_date', DateRangeFilterBuilder()))  # Adiciona o filtro
    readonly_fields = ('formatted_hours_worked', 'formatted_total_value')

    def formatted_total_value(self, obj):
        """Formata o campo total_value com R$."""
        if obj.total_value is not None:
            return f"R$ {obj.total_value:.2f}"
        return "-"
    formatted_total_value.short_description = "Valor Total"
    formatted_total_value.admin_order_field = 'total_value'

    def formatted_hours_worked(self, obj):
        """Formata o campo hours_worked como HH:MM."""
        if obj.hours_worked is not None:
            total_minutes = int(obj.hours_worked * 60)
            hours = total_minutes // 60
            minutes = total_minutes % 60
            return f"{hours:02}:{minutes:02}"
        return "-"
    formatted_hours_worked.short_description = "Horas Trabalhadas"
    formatted_hours_worked.admin_order_field = 'hours_worked'

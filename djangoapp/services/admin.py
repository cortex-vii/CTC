from django.urls import path
from django.utils.html import format_html
from django.contrib import admin
from django.shortcuts import render
from django.urls import reverse
from .models import Service
from entries.models import Entry
from exits.models import Exit

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('client', 'start_date', 'end_date', 'status', 'generate_report_link')
    search_fields = ('client', 'description')
    list_filter = ('status', 'start_date', 'end_date')
    filter_horizontal = ('machines', 'operators')

    def generate_report_link(self, obj):
        # Usa reverse para gerar a URL da view do relatório com base no ID do serviço
        url = reverse('admin:service_report', args=[obj.id])
        return format_html('<a href="{}">Gerar Relatório</a>', url)

    generate_report_link.short_description = 'Relatório'

    def get_urls(self):
        # Adiciona a URL personalizada para o relatório
        urls = super().get_urls()
        custom_urls = [
            path('<int:service_id>/relatorio/', self.admin_site.admin_view(self.generate_html_report), name='service_report'),
        ]
        return custom_urls + urls

    def generate_html_report(self, request, service_id):
        # Busca o serviço e os dados relacionados
        service = Service.objects.get(id=service_id)
        entries = Entry.objects.filter(service=service)
        exits = Exit.objects.filter(service=service)
        
        # Passa os dados para o template
        context = {
            'service': service,
            'entries': entries,
            'exits': exits,
        }
        
        return render(request, 'admin/service_report.html', context)

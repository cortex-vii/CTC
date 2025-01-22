from django.contrib import admin
from .models import Exit

@admin.register(Exit)
class ExitAdmin(admin.ModelAdmin):
    list_display = ('service', 'category', 'quantity', 'exit_date')
    search_fields = ('service__client', 'description')
    list_filter = ('exit_date', 'category')

from django.contrib import admin
from .models import Machine

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'description')
    search_fields = ('name', 'description')
    list_filter = ('status',)

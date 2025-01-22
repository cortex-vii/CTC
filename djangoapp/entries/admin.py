from django.contrib import admin
from .models import Entry

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('service', 'category', 'quantity', 'entry_date')
    search_fields = ('service__client', 'description')
    list_filter = ('entry_date', 'category')

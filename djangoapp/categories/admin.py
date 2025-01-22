from django.contrib import admin
from .models import CategoryExit, CategoryEntry

@admin.register(CategoryExit)
class CategoryExitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(CategoryEntry)
class CategoryEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

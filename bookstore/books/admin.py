from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'author'),
        }),
        ('More Details', {
            'classes': ('collapse',),  # This makes the section collapsible
            'fields': ('isbn', 'price', 'image'),
        }),
    )

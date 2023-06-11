from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Add contact filters to admin panel"""
    list_display = ('email', 'message', 'subject', 'created_on')
    list_filter = ('email', 'subject', 'created_on')
    search_fields = ('email', 'subject')

from django.contrib import admin
from .models import Review


@admin.register(Review)
class Review(admin.ModelAdmin):
    """
    Displays the fields for the Review model
    """
    list_display = ('user', 'product', 'review', 'created_on')

from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class Wishlist(admin.ModelAdmin):
    """
    Displays the fields for the Review model
    """
    list_display = ('user', 'product')

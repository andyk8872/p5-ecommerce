from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('add_to_wishlist/', views.add_to_wish_list, name='add_to_wishlist'),
]

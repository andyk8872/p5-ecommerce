from django.urls import path
from . import views

urlpatterns = [
    path('', views.make_review, name='make_review'),
    path('show_review/', views.show_review, name='show_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>', views.edit_review, name='edit_review'),
]
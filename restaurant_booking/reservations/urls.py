from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
]

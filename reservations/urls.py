from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('make/', views.make_reservation, name='make_reservation'),
    path('my/', views.my_reservations, name='my_reservations'),
    path(
     'cancel/<int:pk>/',
     views.cancel_reservation,
     name='cancel_reservation'
     ),
]


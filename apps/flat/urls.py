from django.urls import path
from apps.flat import views

urlpatterns = [
    path('', views.flats, name='flats'),
]
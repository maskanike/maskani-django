from django.urls import path
from apps.property import views

urlpatterns = [
    path('', views.properties, name='properties'),
]
from django.urls import path
from apps.user import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
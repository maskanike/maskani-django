from django.urls import path
from apps.user import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('<int:user_id>/reset-password/', views.reset, name='password_reset'),
    path('<int:user_id>/', views.update, name='update'),
]
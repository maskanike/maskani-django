from django.contrib import admin
from django.urls import path, include
from django.views import generic


urlpatterns = [
    path('', include('apps.user.urls')),
    path('property/', include('apps.property.urls')),
    path('admin/', admin.site.urls),
]

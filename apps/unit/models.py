from django.db import models
from apps.property.models import Property
class Unit(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    propert  = models.ForeignKey(Property, on_delete=models.CASCADE)

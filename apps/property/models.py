from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    payment_details = models.CharField(max_length=150)
    active = models.BooleanField(default=False)
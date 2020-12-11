from django.db import models



class Flat(models.Model):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
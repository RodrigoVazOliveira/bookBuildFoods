from django.db import models
from datetime import datetime

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    mode_prepare = models.TextField()
    time_prepare = models.IntegerField()
    income = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_time_created = models.DateTimeField(default=datetime.now(), blank=True)





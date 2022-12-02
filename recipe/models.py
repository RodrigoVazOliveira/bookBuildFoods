from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    mode_prepare = models.TextField()
    time_prepare = models.IntegerField()
    income = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date_time_created = models.DateTimeField(default=datetime.now(), blank=True)
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)

    def __str__(self):
        return self.name



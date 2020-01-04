from django.db import models
from datetime import date


# Create your models here.
class Post(models.Model):
    content = models.TextField(max_length=512)
    owner = models.CharField(max_length=20)
    positive_points = models.BigIntegerField()
    negative_points = models.BigIntegerField()
    date = models.DateField(default=date.today())

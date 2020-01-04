from django.db import models
from django.utils.timezone import now
from register.models import User


# Create your models here.
class Post(models.Model):
    content = models.TextField(max_length=512)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    positive_points = models.BigIntegerField()
    negative_points = models.BigIntegerField()
    date = models.DateField(default=now())

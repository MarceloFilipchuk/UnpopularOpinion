from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True, null=False)
    password = models.CharField(max_length=10, null=False)
    token = models.TextField(null=True)
    voted_posts = models.TextField()
    karma = models.BigIntegerField(default=0)

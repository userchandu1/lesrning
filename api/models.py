from django.db import models
from datetime import datetime


class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.now())
    name = models.TextField()
    address = models.CharField(max_length=200)
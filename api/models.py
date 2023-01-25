from django.db import models
from datetime import datetime, timezone


class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    address1 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.email

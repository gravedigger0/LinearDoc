from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class LinkStorage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default='untitled')
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=300)
    visited = models.BooleanField(default=False)
    note = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

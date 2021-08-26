from core.views import title
from django.db import models

# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    images = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


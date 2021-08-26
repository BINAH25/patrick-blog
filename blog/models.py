from django.db import models
from datetime import datetime

# Create your models here.
class Message(models.Model):
    email = models.EmailField(max_length=50)
    date = models.DateTimeField(default=datetime.now, blank=True)

class Post(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

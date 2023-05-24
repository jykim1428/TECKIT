from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField()
    content =models.TextField()
    created_at = models.
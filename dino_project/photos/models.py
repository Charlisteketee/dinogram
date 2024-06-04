from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=100)
  bio = models.TextField(blank=True)

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  image_url = models.URLField()
  caption = models.TextField()



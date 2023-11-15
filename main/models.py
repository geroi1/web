from django.db import models

# Create your models here.
class Arcticle(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
class Comment(models.Model):
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    
class Tags(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
from django.db import models
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=70)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=500)
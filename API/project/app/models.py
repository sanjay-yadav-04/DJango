from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
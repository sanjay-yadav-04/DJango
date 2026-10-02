from django.db import models

# Create your models here.
class Add_to_cart(models.Model):
    name=models.CharField(max_length=50)
    des=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField()
    category=models.CharField(max_length=50)
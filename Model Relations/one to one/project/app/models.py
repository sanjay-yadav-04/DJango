from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadhar_no=models.IntegerField()
    create_date=models.DateField(auto_now=True)
    create_by=models.CharField(max_length=50)

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    a_no=models.OneToOneField(Aadhar,on_delete=models.CASCADE)
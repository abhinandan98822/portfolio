from django.db import models

# Create your models here.
class Viewers(models.Model):
    fullname=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    dob=models.CharField(max_length=60)
    mobile=models.IntegerField()
    gender=models.CharField(max_length=40)

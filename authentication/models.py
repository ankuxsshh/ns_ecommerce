from django.db import models

# Create your models here.
class Customers(models.Model):
    id = models.AutoField( primary_key=True)
    fname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=150,unique=True)
    phone = models.CharField(max_length=10,null=True)
    password = models.CharField(max_length=32,null=True)
    address = models.TextField(null=True,blank=True)
    verified = models.BooleanField(default=False)
    
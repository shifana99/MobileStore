from django.db import models
from account.models import*

# Create your models here.

class Product(models.Model):
    productname=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_image")
    price=models.IntegerField()
    ram=models.CharField(max_length=100)
    rom=models.CharField(max_length=100)
    battery=models.CharField(max_length=100)
    processor=models.CharField(max_length=200)
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name="p_user")
    

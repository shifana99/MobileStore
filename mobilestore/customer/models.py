from django.db import models
from account.models import CustomerUser
from store.models import Product


class Cart(models.Model):
   
    status=models.CharField(max_length=100,default="carted")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="c_product")
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name="cart_user")


class Payment(models.Model):
    bank=models.CharField(max_length=100)
    acholdername=models.CharField(max_length=100) 
    accno=models.IntegerField()
    ifsc=models.CharField(max_length=100)
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE,related_name="u_paayment")  
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="p_payment",null=True)
    quantity=models.PositiveBigIntegerField(null=True)
    status=models.CharField(max_length=100,null=True)





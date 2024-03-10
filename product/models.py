from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="my_product")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()


class BillingAd(models.Model):
    name=models.CharField(max_length=50)
    Address=models.TextField()
    pin_Code=models.IntegerField()
    Mobile_No=models.IntegerField()

    def __str__(self):
        return self.name  

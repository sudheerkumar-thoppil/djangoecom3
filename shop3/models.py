from pyexpat import model
from django.db import models

# Create your models here.
class Products(models.Model):
    prod_name = models.CharField(max_length=50)
    prod_price= models.IntegerField(default=0)
    prod_image=models.ImageField(upload_to='media')

    def __str__(self):
        return self.prod_name


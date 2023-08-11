from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

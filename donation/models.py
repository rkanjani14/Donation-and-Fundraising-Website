from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=250)
    amount = models.DecimalField(max_digits=7,decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
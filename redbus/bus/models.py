from django.db import models

# Create your models here.
class bus_details(models.Model):
    bname = models.CharField(max_length=20)
    bdate = models.DateField()
    bprice = models.FloatField()
    bfrom = models.CharField(max_length=20)
    bto = models.CharField(max_length=20)

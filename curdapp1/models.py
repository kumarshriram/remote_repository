

from django.db import models

class ProductData(models.Model):
    pid=models.IntegerField()
    pname=models.CharField(max_length=100)
    pcost=models.IntegerField()
    pclass=models.CharField(max_length=100)
    npros=models.IntegerField()
    mdate=models.DateTimeField(max_length=100)
    edate=models.DateTimeField(max_length=100)
    cname=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)

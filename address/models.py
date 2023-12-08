from django.db import models

# Create your models here.
class Address(models.Model):
    # AutoField => auto_increment, primary_key 지정
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)


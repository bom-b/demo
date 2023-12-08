from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(null=False,max_length=150)
    price = models.IntegerField(default=0)
    description = models.TextField(null=False,max_length=150)
    picture_url = models.CharField(null=True,max_length=150)

# class UpFile(models.Model):
#     upfile_id = models.AutoField(primary_key=True)
#     upfile_name = models.CharField(null=False,max_length=150)
#     upfile_url = models.CharField(null=True, max_length=150)
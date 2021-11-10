from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    price = models.PositiveBigIntegerField(blank=False)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=False, default=20)
    active = models.BooleanField(default=True, blank=False)


class Post(models.Model):
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(blank=False, )
    image = models.ImageField(upload_to='post/')


class ContactInfo(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=70, blank=False)
    comment = models.TextField(blank=False)

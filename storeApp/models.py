from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


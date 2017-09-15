# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=2000)
    price = models.IntegerField(default=0)
    photo = models.FileField()

    def __str__(self):
        return self.title

class Enquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    enq = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('shop:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return str(self.product)

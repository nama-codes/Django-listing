# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_ID = models.EmailField()
    phone = models.BigIntegerField()
    country = models.CharField(max_length=20)
    message = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('contact:contact',kwargs={'pk':self.pk})

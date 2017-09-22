# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Product, Enquiry, Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title','description']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Enquiry)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from .models import Enquiry,Product
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    template_name = 'shop/index.html'

    def get_queryset(self):
        return Product.objects.all()

class DetailView(generic.DetailView):
    model = Product
    template_name = 'shop/detail.html'

class Enquire(CreateView):
    model = Enquiry
    fields = ['name','email','enq','product']
    template_name = 'shop/enquiry_form.html'

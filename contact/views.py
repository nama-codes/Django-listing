# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from .models import Contact
from django.views.generic.edit import CreateView
from shop.models import Category
# Create your views here.
class ContactView(CreateView):
    model = Contact
    fields = ['first_name','last_name','email_ID','phone','country','message']
    template_name = 'contact/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['cat'] = Category.objects.all()
        return context

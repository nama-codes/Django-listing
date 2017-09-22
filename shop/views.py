# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from .models import Enquiry,Product, Category
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    context_object_name = "product_list"
    queryset = Product.objects.all()
    template_name='shop/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cat'] = Category.objects.all()
        return context

class Category_list_View(generic.ListView):
    context_object_name = 'category_list'
    queryset = Category.objects.all()
    template_name='shop/base.html'



class CategoryView(generic.DetailView):
    model = Category
    template_name = 'shop/category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['cat'] = Category.objects.all()
        return context

class DetailView(generic.DetailView):
    model = Product
    template_name = 'shop/detail.html'
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['cat'] = Category.objects.all()
        return context

class Enquire(CreateView):
    model = Enquiry
    fields = ['name','email','enq','product']
    template_name = 'shop/enquiry_form.html'

    def get_context_data(self, **kwargs):
        context = super(Enquire, self).get_context_data(**kwargs)
        context['cat'] = Category.objects.all()
        return context

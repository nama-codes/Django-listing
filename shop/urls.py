from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^category/$', views.Category_list_View.as_view(), name = 'category_list'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name = 'category'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'^(?P<pk>[0-9]+)/enquire/$', views.Enquire.as_view(), name = 'enquire'),

]

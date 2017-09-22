from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'contact'
urlpatterns = [
    url(r'^$', views.ContactView.as_view(), name = 'contact'),
]

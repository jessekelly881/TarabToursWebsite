from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', views.tours),
    url('vegan', views.vegan),
]

from django.shortcuts import render
import copy
import django_project

def aboutBaseData():
    base = copy.copy(django_project.views.base_variables)
    base['title'] = 'About Us'
    return base

def about(request):
    return render(request, 'about.html',{'base_variables': aboutBaseData()})

from django.shortcuts import render
import copy
import django_project

base = copy.copy(django_project.views.base_variables)
base['title'] = 'Contact Us'

def contact(request):
    return render(request, 'contact.html', {'base_variables': base})

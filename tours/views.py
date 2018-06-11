from django.shortcuts import render
from tours.models import TourType
import django_project, copy

def tours(request):
    tours = TourType.objects.all()
    base = copy.copy(django_project.views.base_variables)
    base['title'] = 'Our Tours'
    return render(request, 'tours.html', {'tours': tours, 'base_variables': base})

def vegan(request):
    base = copy.copy(django_project.views.base_variables)
    base['title'] = 'Vegan Adventure'
    return render(request, 'vegan.html',{'base_variables': base})

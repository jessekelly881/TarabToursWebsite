from django.shortcuts import render
import random

base_variables = {
    'title': 'Tarab Tours',
    'nav_bar_links':[
        {'name': 'Tours', 'url':'/tours', 'hide_mid_down': False},
        {'name': 'Book', 'url':'/book','hide_mid_down': False},
        {'name': 'Contact Us', 'url':'/contact','hide_mid_down': False},
        {'name': 'Blog', 'url':'/blog', 'hide_mid_down': True},
        {'name': 'About Us', 'url':'/about','hide_mid_down': True},
        {'name': 'FAQ', 'url':'/faq','hide_mid_down': True},
    ],
    'contact' : {
        'email': 'contact@tarabtours.com',
        'phone': '+1 (614) 721-7379'
        },
    'links' : [
        {'name': 'Blog', 'url': '/blog'},
        {'name': 'About Us', 'url': '/about'},
        {'name': 'FAQ', 'url': '/faq'},
    ],
    'social' : {
        'facebook': 'https://www.facebook.com/tarabtours/',
        'twitter' : 'https://www.twitter.com',
        'instagram': 'https://www.instagram.com/tarabmexico/'
    },

    'copyright_lines' : ['Jesse Kelly', 'admin@tarabtours.com'],
}

def home(request):
    return render(request, 'home.html', {'base_variables':base_variables})

def base(request):
    return render(request, 'base.html',{'base_variables':base_variables})

def test(request):
    return render(request, 'test.html')

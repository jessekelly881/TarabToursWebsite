from django.shortcuts import render
from django import forms
import django_project
import copy
import pycountry
from handle_booking import handleBooking
from django.http import HttpResponseRedirect


PAYMENT_METHODS = [
    {'name': 'Credit Card', 'code': 'credit'},
    {'name': 'Crypto Currency', 'code': 'crypto'},
    {'name': 'Paypal', 'code': 'paypal'},
    #{'name': 'Apple Pay', 'code': 'apple'},
    #{'name': 'Google Pay', 'code': 'google'},
    ]

TERMS_CONDITIONS = """
Harry Potter and the Sorcerer's Stone.

CHAPTER ONE - THE BOY WHO LIVED.

Mr. and Mrs. Dursley, of number four, Privet Drive,
were proud to say that they were perfectly normal,
thank you very much. They were the last people you'd expect
to be involved in anything strange or mysterious, because
they just didn't hold with such nonsense.
"""

tours = [
    {'name': 'Vegan Food Tour', 'date': 'Thurs. May 18', 'time':'12:30-4:30', 'cost': '55.95', 'spaces': 2},
    {'name': 'Vegan Food Tour', 'date': 'Thurs. May 19', 'time':'12:30-4:30', 'cost': '55.95', 'spaces': 5},
    {'name': 'Some Other Tour', 'date': 'Thurs. May 22', 'time':'12:30-4:30', 'cost': '105.95', 'spaces': 1},
    {'name': 'Vegan Food Tour', 'date': 'Thurs. May 25', 'time':'12:30-4:30', 'cost': '55.95', 'spaces': 3},
    ]

class PersonalInfo(forms.Form):

    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    confirm_email = forms.EmailField()
    phone = forms.CharField(max_length=30)
    confirm_phone = forms.CharField(max_length=30)

    #tour = forms.ChoiceField(choices=(("A", "B"), ("C", "D")))

def book(request):
    if request.method == 'POST':
        (success, confirmation_num) = handleBooking(request)
        url = '/book/success/?num=' + str(confirmation_num)
        if success: return HttpResponseRedirect(url)


    base = copy.copy(django_project.views.base_variables)
    base['title'] = 'Book A Tour'

    personal = PersonalInfo()
    return render(request, 'book.html',
        {
            'form': personal,
            'payment_types': PAYMENT_METHODS,
            'tours': tours,
            'base_variables': base,
            'terms': TERMS_CONDITIONS,
            'countries': list(pycountry.countries),
        })


def success(request):
    base = copy.copy(django_project.views.base_variables)
    base['title'] = 'Success!'

    return render(request, 'success.html', {'base_variables': base})

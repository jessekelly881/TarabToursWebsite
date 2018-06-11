from django.contrib import admin
from .models import Person, Booking, Tour

admin.site.register(Tour)
admin.site.register(Person)
admin.site.register(Booking)

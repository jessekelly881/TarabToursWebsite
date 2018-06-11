from django.db import models


class Tour(models.Model):
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Tour'

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + self.last_name

    class Meta:
        verbose_name = 'Person'

class Booking(models.Model):
    date_time_booked = models.DateTimeField(auto_now_add = True)
    confirmation_number = models.IntegerField()
    #payment_method =
    #booked_by = models.ForeignKey('Person', default=1) #TODO: on_delete=models.CASCADE? #TODO: Figure out why I can't reference this.
    #tour = models.ForeignKey('Tour', default=1)

    class Meta:
        verbose_name = 'Booking'

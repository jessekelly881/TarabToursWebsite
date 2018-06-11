from django.db import models

class TourType(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField()
    description = models.TextField()
    #main_img = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Available Tour'

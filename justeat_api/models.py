from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    cuisines = models.ManyToManyField('Cuisine')


class Cuisine(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

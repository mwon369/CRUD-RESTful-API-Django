from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name

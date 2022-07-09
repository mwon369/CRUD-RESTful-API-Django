from django.db import models

class Pizza(models.Model):

    SIZE_CHOICES = [
        ("L", "Large"),
        ("M", "Medium"),
        ("S", "Small"),
    ]

    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    price = models.FloatField()
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, default="M")
    isVegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name

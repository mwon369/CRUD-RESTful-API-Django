from django.db import models

# a blueprint for pizza objects that will be stored in our database
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

    # override __str__ method to display name on admin panel
    def __str__(self):
        return self.name

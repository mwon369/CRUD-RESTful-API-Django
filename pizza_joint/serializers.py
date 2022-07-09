from rest_framework import serializers
from .models import Pizza

class PizzaSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['id', 'name', 'ingredients', 'price', 'size', 'isVegeterian']
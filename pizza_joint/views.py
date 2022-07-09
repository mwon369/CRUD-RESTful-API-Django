from django.http import JsonResponse
from .models import Pizza
from .serializers import PizzaSeralizer

# method will retrive list of pizza data and return it in JSON 
def pizza_list(request):
    pizzas = Pizza.objects.all() # get list as query set
    serealizer = PizzaSeralizer(pizzas, many=True) # serialize
    return JsonResponse(serealizer.data, safe=False) # convert serialized data to JSON
from django.http import JsonResponse
from .models import Pizza
from .serializers import PizzaSeralizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# method will retrive list of pizza data and return it in JSON 
@api_view(['GET', 'POST'])
def pizza_list(request):

    if request.method == 'GET':
        pizzas = Pizza.objects.all() # get list as query set
        serializer = PizzaSeralizer(pizzas, many=True) # serialize
        return JsonResponse({"pizza": serializer.data}) # convert serialized data to JSON

    if request.method == 'POST':
        serializer = PizzaSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
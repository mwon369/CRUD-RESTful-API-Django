from django.http import JsonResponse
from .models import Pizza
from .serializers import PizzaSeralizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def pizza_list(request):
    # get query set of all pizza objects, serialize it and convert to JSON
    if request.method == 'GET':
        pizzas = Pizza.objects.all()
        serializer = PizzaSeralizer(pizzas)
        return Response(serializer.data)

    # get POST data, deserialize it and save object to the database
    elif request.method == 'POST':
        serializer = PizzaSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def pizza_detail(request, id):
    # get pizza object with id requested
    try:
        pizza = Pizza.objects.get(pk=id)
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # return pizza object data after serializing
    if request.method == 'GET':
        serializer = PizzaSeralizer(pizza)
        return Response(serializer.data)

    # similar to POST method; deserialize updated data related to a specific pre-existing pizza object
    elif request.method == 'PUT':
        serializer = PizzaSeralizer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from django.shortcuts import render
from rest_framework.views import *
from rest_framework.generics import *
from rest_framework.mixins import *
from .models import *
from .serializer import *
from django_filters.rest_framework import *
# Create your views here.

# we can use ListCreateAPIView , 
# which can do both list as well as Create
class MakePizza(CreateAPIView):
    queryset=Pizza.objects.all()
    serializer_class=PizzaSlr

class ModifyPizza(RetrieveUpdateDestroyAPIView):
    queryset=Pizza.objects.all()
    serializer_class=PizzaSlr


class ListPizza(ListAPIView):
    queryset=Pizza.objects.all()
    serializer_class=PizzaSlr_List
    filter_backends=[DjangoFilterBackend]
    filterset_fields =['types','sizes']



    

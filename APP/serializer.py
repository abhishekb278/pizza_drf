from rest_framework import serializers
from .models import *

class PizzaSlr(serializers.ModelSerializer):
    class Meta:
        model=Pizza
        fields=['pid','types','sizes','toppings']

class PizzaSlr_List(serializers.ModelSerializer):
    sizes=serializers.SerializerMethodField('get_size_name')
    toppings=serializers.SerializerMethodField('get_topping_name')
    class Meta:
        model=Pizza
        fields=['pid','types','sizes','toppings']

    def get_size_name(self,obj):
        a=str(obj.sizes)
        return a
    def get_topping_name(self,obj):
        a=str(obj.toppings)
        return a
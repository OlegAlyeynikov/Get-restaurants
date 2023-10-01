from rest_framework import serializers
from .models import Restaurant, Cuisine


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ('name',)


class RestaurantSerializer(serializers.ModelSerializer):
    cuisines = CuisineSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('name', 'rating', 'cuisines')

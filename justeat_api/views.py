from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Restaurant, Cuisine
from .serializer import RestaurantSerializer


class RestaurantListView(APIView):
    def get(self, request, postal_code):

        api_url = f"https://api.just-eat.com/restaurants/bypostcode/{postal_code}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            restaurants = []

            for restaurant_data in data['Restaurants']:
                cuisines = restaurant_data['Cuisines']
                restaurant, created = Restaurant.objects.get_or_create(
                    name=restaurant_data['Name'],
                    rating=restaurant_data['RatingStars'],
                )

                for cuisine_name in cuisines:
                    cuisine, _ = Cuisine.objects.get_or_create(name=cuisine_name)
                    restaurant.cuisines.add(cuisine)

                restaurants.append(restaurant)

            serializer = RestaurantSerializer(restaurants, many=True)
            return Response(serializer.data)

        return Response(
            {"detail": "Failed to fetch restaurant data from Just Eat API"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

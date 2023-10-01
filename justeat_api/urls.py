from django.urls import path
from justeat_api.views import RestaurantListView

urlpatterns = [
    path('restaurants/<str:postal_code>/', RestaurantListView.as_view(), name='restaurant-list'),
]

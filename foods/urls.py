from django.urls import path
from .views import FoodView, FoodDetailView, WeekAPIView, CategoryApiView

urlpatterns  = [
    path("api/v1/foods/", FoodView.as_view(), name = "foods"),
    path('api/v1/foods/<int:pk>/', FoodDetailView.as_view(),name='food'),
    path("api/v1/week-recs/", WeekAPIView.as_view(), name="weeks"),
    path("api/v1/categories/", CategoryApiView.as_view(), name="categories")
]
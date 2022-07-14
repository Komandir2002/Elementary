from rest_framework import serializers
from .models import Food, Weeks, Category
from .models import WEEK_CHOICES



class CategorySeriazlier(serializers.Serializer):
    category = serializers.CharField(max_length=50)
    category_type = serializers.CharField(max_length=50)

    class Meta:
        model = Category
        fields = ["category", "category_type"]




class WeekSerializer(serializers.Serializer):
    week = serializers.CharField(max_length=50)
    food = serializers.CharField(max_length=255)
    class Meta:
        model = Weeks
        fields = ['week', 'food']





class FoodSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=45)
    calories = serializers.FloatField(default=0.0)
    price = serializers.FloatField(default=0.0)
    week_choices = serializers.CharField(default=WEEK_CHOICES[0][0])
    class Meta:
        model = Food
        fields = ["id,","title", "calories", "price", "week_choices"]



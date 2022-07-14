from django.shortcuts import render,get_object_or_404
from .models import Food, Category, Weeks
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser, AllowAny
from django.core.exceptions import ObjectDoesNotExist


class CategoryApiView(generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySeriazlier
    permission_classes = [AllowAny]

    def get(self, request):
        category = Category.objects.all()
        serializers = self.serializer_class(instance=category, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(customer=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class WeekAPIView(generics.GenericAPIView):
    queryset = Weeks.objects.all()
    serializer_class = serializers.WeekSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        week = Weeks.objects.all()
        serializers = self.serializer_class(instance=week, many=True)
        return Response(data=serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(customer=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class FoodView(generics.GenericAPIView):
    queryset = Food.objects.all()
    serializer_class = serializers.FoodSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        foods = Food.objects.all()
        serializers = self.serializer_class(instance=foods, many=True)

        return Response(data=serializers.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(customer=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class FoodDetailView(generics.GenericAPIView):
    serializer_class = serializers.FoodSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)

        serializer = self.serializer_class(instance=food)

        return Response(data=serializer.data,status=status.HTTP_200_OK)


    def put(self, request, pk):

        food = get_object_or_404(Food, pk=pk)

        serializer = self.serializer_class(instance=food, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


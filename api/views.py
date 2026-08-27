from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from storeapp.models import Product, Category

class api_products(ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerial


class api_product(RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerial

class api_categories(ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerial


class api_category(RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerial
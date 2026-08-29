from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from storeapp.models import Product, Category
from .filter import *

class Products_View_Set(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerial
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = Products_filter
    search_fields = ['name', 'description']
    ordering_fields = ['old_price', 'name']


class Categories_View_Set(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerial
from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
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
    pagination_class = PageNumberPagination


class Categories_View_Set(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerial

class Review_View_Set(ModelViewSet):

    # queryset = Review.objects.all()
    serializer_class = Review_Serializer

    def get_serializer_context(self):
        return {'product_id' : self.kwargs['product_pk']}
    
    def get_queryset(self):

        return Review.objects.filter(product_id=self.kwargs['product_pk'])

class Cart_View_Set(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):

    queryset= Cart.objects.all()
    serializer_class = Cart_Serializer

class CartItem_View_Set(ModelViewSet):

    # queryset = Cartitems.objects.all()
    # serializer_class = Cart_item_serializer

    def get_serializer_class(self):

        if self.request.method=='POST':
            return add_cart_item_serializer

        else:
            return Cart_item_serializer

    def get_serializer_context(self):
        return {'cart_id' : self.kwargs['cart_pk']}

    def get_queryset(self):
        return Cartitems.objects.filter(cart_id=self.kwargs['cart_pk'])


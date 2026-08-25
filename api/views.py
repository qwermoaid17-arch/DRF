from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from storeapp.models import Product, Category

@api_view()
def api_products(request):

    products = Product.objects.all()
    serial = ProductSerial(products, many = True)

    return Response(serial.data)

@api_view()
def api_product(request, pk):

    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerial(product)
    return Response(serializer.data)

@api_view()
def api_categories(request):

    categories = Category.objects.all()
    serial = CategorySerial(categories, many = True)
    return Response(serial.data)

@api_view()
def api_category(request, pk):

    category = get_object_or_404(Category, category_id=pk)
    serializer = CategorySerial(category)
    return Response(serializer.data)
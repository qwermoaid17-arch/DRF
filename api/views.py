from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from .serializers import *
from storeapp.models import Product, Category

@api_view(['GET', 'POST', 'PUT'])
def api_products(request):

    if request.method=='GET':

        products = Product.objects.all()
        serial = ProductSerial(products, many = True)
        return Response(serial.data)
    
    if request.method=='POST':
        serializer = ProductSerial(data = request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method=='PUT':

        pk = request.data.get('id')

        product = get_object_or_404(Product, id=pk)

        serializer = ProductSerial(product, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

@api_view(['GET',  'PUT', 'PATCH', 'DELETE'])
def api_product(request, pk):
        
    product = get_object_or_404(Product, id=pk)

    if request.method=='GET':

        serializer = ProductSerial(product)
        return Response(serializer.data)
    
    if request.method=='PUT':

        serializer= ProductSerial(product, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=200)
    
    if request.method=='PATCH':

        serializer= ProductSerial(product, data = request.data, partial= True)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=200)

    if request.method=='DELETE':

        product.delete()

        return Response(status=HTTP_204_NO_CONTENT)
        
        
@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def api_categories(request):

    if request.method=='GET':

        categories = Category.objects.all()
        serial = CategorySerial(categories, many = True)
        return Response(serial.data)
    
    if request.method=='POST':

        serializer = CategorySerial(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    
    if request.method=='PUT':

        pk = request.data.get('category_id')

        categor = get_object_or_404(Category, category_id=pk)

        serializer = CategorySerial(categor, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method=='PATCH':

        pk = request.data.get('category_id')

        categor = get_object_or_404(Category, category_id=pk)

        serializer = CategorySerial(categor, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def api_category(request, pk):

    
    categor = get_object_or_404(Category, category_id=pk)

    if request.method=='GET':

        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerial(category)
        return Response(serializer.data)
    
    if request.method=='POST':

        serializer=CategorySerial(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data )

    if request.method=='PUT':

        serializer= CategorySerial(categor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method=='PATCH':

        serializer= CategorySerial(categor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    if request.method=='DELETE':

        categor.delete()

        return Response(status=HTTP_204_NO_CONTENT)
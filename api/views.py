from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .serializers import *
from storeapp.models import Product, Category

class api_products(APIView):

    def get(self, request):

        products = Product.objects.all()
        serial = ProductSerial(products, many = True)
        return Response(serial.data) gggsfdds

    def post(self, request):

        serializer = ProductSerial(data = request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request):

        pk = request.data.get('id')

        product = get_object_or_404(Product, id=pk)

        serializer = ProductSerial(product, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

class api_product(APIView):

    def get(self, request, pk):

        
        product = get_object_or_404(Product, id=pk)

        serializer = ProductSerial(product)
        return Response(serializer.data)

    def put(self, request,pk):

        product = get_object_or_404(Product, id=pk)

        serializer= ProductSerial(product, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=200)

    def patch(self, request, pk):

        product = get_object_or_404(Product, id=pk)

        serializer= ProductSerial(product, data = request.data, partial= True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=200)

    def delete(self, request, pk):

        product = get_object_or_404(Product, id=pk)

        product.delete()

        return Response(status=HTTP_204_NO_CONTENT)    

class api_category(APIView):

    def get(self, request, pk):

        category = get_object_or_404(Category, category_id=pk)
        serializer = CategorySerial(category)
        return Response(serializer.data)


    def put(self, request,pk):

        categor = get_object_or_404(Category, category_id=pk)

        serializer= CategorySerial(categor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



    def patch(self, request, pk):

        categor = get_object_or_404(Category, category_id=pk)

        serializer= CategorySerial(categor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):

        categor = get_object_or_404(Category, category_id=pk)
  
        categor.delete()

        return Response(status=HTTP_204_NO_CONTENT)


class api_categories(APIView):

    def get(self, request):

        categories = Category.objects.all()
        serial = CategorySerial(categories, many = True)
        return Response(serial.data)


    def post(self, request):

        serializer = CategorySerial(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


    def put(self, request):

        pk = request.data.get('category_id')

        categor = get_object_or_404(Category, category_id=pk)

        serializer = CategorySerial(categor, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request):

        pk = request.data.get('category_id')

        categor = get_object_or_404(Category, category_id=pk)

        serializer = CategorySerial(categor, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
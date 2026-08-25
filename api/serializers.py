from rest_framework import serializers
from storeapp.models import *

class ProductSerial(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['id', 'name', 'description', 'category', 'slug', 'inventory', 'old_price', 'price']

class CategorySerial(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = ['category_id', 'title',  'slug']
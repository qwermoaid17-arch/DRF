from rest_framework import serializers
from storeapp.models import *

class CategorySerial(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = ['category_id', 'title',  'slug']


class ProductSerial(serializers.ModelSerializer):

    category = CategorySerial()

    class Meta:

        model = Product
        fields = ['id', 'name', 'description', 'category', 'slug', 'inventory', 'old_price', 'price']

class Review_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Review
        fields = ['id', 'date_created', 'name', 'description']

    def create(self, validated_data):

        product_id = self.context['product_id']
        return Review.objects.create(product_id = product_id, **validated_data)
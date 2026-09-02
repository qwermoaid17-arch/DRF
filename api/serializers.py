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

class single_product_serial(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ['name', 'old_price']

class Cart_item(serializers.ModelSerializer):

    product = single_product_serial(many=False)
    sub_total = serializers.SerializerMethodField(method_name='total')

    def total(self, caart:Cartitems):

        return caart.quantity * caart.product.price
    
    class Meta:
        model = Cartitems
        fields = ['id','cart', 'product', 'quantity', 'sub_total']
    
class Cart_Serializer(serializers.ModelSerializer):

    cart_id = serializers.UUIDField(read_only=True)
    items = Cart_item(many=True, read_only=True)

    def main_total(self, cart: Cart):

        items = cart.items.all()
        total = sum([ item.quantity * item.product.price for item in items])
        return total

    big_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:

        model = Cart
        fields = ['cart_id', 'items', 'big_total']
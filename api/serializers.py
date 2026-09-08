from rest_framework import serializers
from storeapp.models import *

class CategorySerial(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = ['category_id', 'title',  'slug']

class ProductImageSerial(serializers.ModelSerializer):

    class Meta:

        model = ProductImage
        fields = ['id','product' ,'image']

class ProductSerial(serializers.ModelSerializer):


    images= ProductImageSerial(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file = False, use_url=False),
        write_only=True
    )

    class Meta:

        model = Product
        fields = ['id', 'name', 'description', 'inventory', 'old_price', 'price', 'images', 'uploaded_images']

    def create(self,validated_data):

        uploaded_images=validated_data.pop('uploaded_images')

        product = Product.objects.create(**validated_data)
        for image in uploaded_images:

            new_product_image = ProductImage.objects.create(product=product, image=image)

        return product

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

class Cart_item_serializer(serializers.ModelSerializer):

    product = single_product_serial(many=False)
    sub_total = serializers.SerializerMethodField(method_name='total')

    def total(self, caart:Cartitems):

        return caart.quantity * caart.product.price
    
    class Meta:
        model = Cartitems
        fields = ['id','cart', 'product', 'quantity', 'sub_total']

class add_cart_item_serializer(serializers.ModelSerializer):

    product_id = serializers.UUIDField()

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('no valid product id try again')
        return value


    def save(self, **kwargs):

        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:

            cart_item = Cartitems.objects.get(product_id=product_id, cart_id=cart_id)
            cart_item.quantity+=quantity
            cart_item.save()
            self.instance = cart_item

        except:
           self.instance = Cartitems.objects.create(cart_id=cart_id, **self.validated_data)
        return self.instance
    class Meta:
        model = Cartitems
        fields = ['id', 'product_id', 'quantity']

class Updata_cart_items_serializer(serializers.ModelSerializer):

    class Meta:
        model = Cartitems
        fields = ['quantity']
    
class Cart_Serializer(serializers.ModelSerializer):

    cart_id = serializers.UUIDField(read_only=True)
    items = Cart_item_serializer(many=True, read_only=True)

    def main_total(self, cart: Cart):

        items = cart.items.all()
        total = sum([ item.quantity * item.product.price for item in items])
        return total

    big_total = serializers.SerializerMethodField(method_name='main_total')

    

    class Meta:

        model = Cart
        fields = ['cart_id', 'items', 'big_total']

class OrderItem_serializer(serializers.ModelSerializer):

    product = single_product_serial()

    total = serializers.SerializerMethodField()

    def get_total(self, order_item: OrderItem):
        return order_item.quantity * order_item.product.price
    

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'total']

class Order_serializer(serializers.ModelSerializer):

    items = OrderItem_serializer(many=True, read_only=True)

    def main_total(self, order: Order):

        items = order.items.all()
        total = sum([ item.quantity * item.product.price for item in items])
        return total

    big_total = serializers.SerializerMethodField(method_name='main_total')

    class Meta:
        model = Order
        fields = ('id', 'placed_at', 'pending_status', 'owner', 'items', 'big_total')

class Profile_serializer(serializers.ModelSerializer):

    class Meta:

        model = profile
        fields = ['id', 'name', 'bio', 'image']
from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()

router.register('products', Products_View_Set)
router.register('categories', Categories_View_Set)
router.register('carts', Cart_View_Set)
router.register('profile', Profile_View_Set)
router.register('orders', Order_View_Set, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', Review_View_Set, basename='reviews')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItem_View_Set, basename='cart-items')

# urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
    path('', include(cart_router.urls))
]
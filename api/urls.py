from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import *

router = routers.DefaultRouter()

router.register('products', Products_View_Set)
router.register('categories', Categories_View_Set)
router.register('carts', Cart_View_Set)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', Review_View_Set, basename='reviews')

# urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls))
]
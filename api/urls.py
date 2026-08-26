from django.urls import path
from .views import *

urlpatterns = [
    path('products/', api_products),
    path('products/<str:pk>', api_product),
    path('categories/', api_categories),
    path('categoies/<str:pk>', api_category)
]
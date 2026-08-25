from django.urls import path
from .views import *

urlpatterns = [
    path('products/', api_products),
    path('products/<str:pk>', api_product),
    path('category/', api_categories),
    path('category/<str:pk>', api_category)
]
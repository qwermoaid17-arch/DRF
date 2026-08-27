from django.urls import path
from .views import *

urlpatterns = [
    path('products/', api_products.as_view()),
    path('products/<str:pk>', api_product.as_view()),
    path('categories/', api_categories.as_view()),
    path('categories/<str:pk>', api_category.as_view())
]
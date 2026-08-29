from django_filters.rest_framework import FilterSet
from storeapp.models import *

class Products_filter(FilterSet):

    class Meta:

        model = Product
        fields = {'category' : ['exact'],
                  'old_price' : ['gt', 'lt', 'exact'],}
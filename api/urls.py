from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('products', Products_View_Set)
router.register('categories', Categories_View_Set)

# urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]
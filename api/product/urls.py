from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"category", CategoryViewSet)
router.register(r"product", ProductViewSet)

app_name = "product_api"
urlpatterns = [
    path("", include(router.urls), name="category-api"),
    path("", include(router.urls), name="product-api"),
]

from django.urls import path
from .views import *

app_name = "product_api"
urlpatterns = [
    path("category/", CategoryViewSet.as_view({"get": "list"}), name="category-api"),
    path("brand/", BrandViewSet.as_view({"get": "list"}), name="brand-api"),
    path("product/", ProductViewSet.as_view({"get": "list"}), name="product-api"),
]

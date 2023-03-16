from django.urls import path
from .views import *

app_name = "product_api"
urlpatterns = [
    path("category/", CategoryViewSet.as_view({"get": "list"}), name="category-api")
]

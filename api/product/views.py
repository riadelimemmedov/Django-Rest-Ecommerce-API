#!Django
from django.shortcuts import render

#!Django Rest
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets


#!Serializers and Models
from .models import *
from .serializers import *


#!Third Party
from drf_spectacular.utils import extend_schema

# Create your views here.


# *CategoryView
class CategoryViewSet(viewsets.ViewSet):
    """
    A Viewset for viewing all category
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#!BrandViewSet
class BrandViewSet(viewsets.ViewSet):
    """
    A Viewset for viewing all brand
    """

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#!BrandViewSet
class ProductViewSet(viewsets.ViewSet):
    """
    A Viewset for viewing all product
    """

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Django and Django Rest
from rest_framework import serializers


# Models
from .models import *


#!CategorySerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


#!BrandSerializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


#!ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = "__all__"


#!ProductLineSerializer
class ProductLineSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductLine
        fields = "__all__"

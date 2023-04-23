# Django and Django Rest
from rest_framework import serializers


# Models
from .models import *


#!CategorySerializer
class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.CharField(source="parent.name", read_only=True)

    class Meta:
        model = Category
        fields = ["name", "parent"]


#!BrandSerializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ["id"]


#!ProductImageSerializer
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ["id", "productline"]


#!AttributeSerializer
class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ["name", "id"]


#!AttributeValueSerializer
class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer(many=False)

    class Meta:
        model = AttributeValue
        fields = ["attribute", "attr_value"]


#!ProductLineSerializer
class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)
    attribute_value = AttributeValueSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = [
            "price",
            "sku",
            "stock_qty",
            "order",
            "product_image",
            "attribute_value",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop("attribute_value")
        attr_values = {}
        for key in av_data:
            attr_values.update({key["attribute"]["id"]: key["attr_value"]})
        data.update({"specification": attr_values})
        return data


#!ProductSerializer
class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name")
    category = CategorySerializer()
    products = ProductLineSerializer(many=True)
    attribute = serializers.SerializerMethodField()
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "brand_name",
            "is_active",
            "pr_slug",
            "description",
            "category",
            "products",
            "attribute",
        ]

    def get_attribute(self, obj):
        attribute = Attribute.objects.filter(product_type_attribute=obj.id)
        return AttributeSerializer(attribute, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop("attribute")
        attr_values = {}
        for key in av_data:
            attr_values.update({key["id"]: key["name"]})
        data.update({"type specification": attr_values})
        return data

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     product_price = []
    #     for i in range(0, len(data["products"])):
    #         product_price.append(
    #             str(ProductLine.objects.get(pk=data["products"][i]).price)
    #         )
    #     data["products"] = product_price
    #     return data

import factory
from api.product.models import Category, Brand, Product


#!CategoryFactory
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test_category"


#!BrandFactory
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = "test_brand"


# #!ProductFactory
# class ProductFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Product

#     name = "test_product"

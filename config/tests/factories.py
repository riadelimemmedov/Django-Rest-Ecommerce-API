# Factories
import factory

# Models
from api.product.models import Category, Brand, Product, ProductLine


#!CategoryFactory
class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "Category_%d" % n)


#!BrandFactory
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "Brand_%d" % n)


#!ProductFactory
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: "Product_%d" % n)
    description = "test_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_active = True


#!ProductLineFactory
class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = "10.00"
    sku = "B700DD1FA82"
    stock_qty = 2
    product = factory.SubFactory(ProductFactory)
    is_active = True

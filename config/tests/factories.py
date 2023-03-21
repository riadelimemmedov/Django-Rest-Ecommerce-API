# Factories
import factory

# Models
from api.product.models import Category, Brand, Product


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

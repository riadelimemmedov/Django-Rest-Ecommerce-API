# Factories
import factory

# Models
from api.product.models import (
    Category,
    Brand,
    Product,
    ProductLine,
    ProductImage,
    ProductType,
    Attribute,
    AttributeValue,
    ProductTypeAttribute,
)


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


#!AttributeFactory
class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attribute

    name = "attribute_name_test"
    description = "attr_description_test"


#!ProductTypeFactory
class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = "test_type"

    @factory.post_generation
    def attribute(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.attribute.add(**extracted)


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
    product_type = factory.SubFactory(ProductTypeFactory)


#!AttributeValueFactory
class AttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AttributeValue

    attr_value = "attr_test"
    attribute = factory.SubFactory(AttributeFactory)


#!ProductLineFactory
class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = "10.00"
    sku = "B700DD1FA82"
    stock_qty = 2
    product = factory.SubFactory(ProductFactory)
    is_active = True

    @factory.post_generation
    def attribute_value(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        print("Extracted Value ProductLine ", extracted)
        self.attribute_value.add(*extracted)


#!ProductImageFactory
class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    alternative_text = "test alternative text"
    product_image_url = "test.png"
    productline = factory.SubFactory(ProductLineFactory)

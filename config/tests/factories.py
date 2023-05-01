# Factories
import factory

# Models
from api.product.models import (
    Category,
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

    name = factory.Sequence(lambda n: "Category_Name_%d" % n)
    ctg_slug = factory.Sequence(lambda n: "Category_Slug_%d" % n)


# #!ProductTypeFactory
class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType

    name = factory.Sequence(lambda n: "Product_Type_%d" % n)

    @factory.post_generation
    def attribute(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.attribute.add(**extracted)


# #!AttributeFactory
class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attribute

    name = "attribute_name_test"
    description = "attr_description_test"


# #!ProductFactory
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: "Product_Name_%d" % n)
    description = "test_product_description"
    is_digital = True
    pid = factory.Sequence(lambda n: "0000_%d" % n)
    category = factory.SubFactory(CategoryFactory)
    is_active = True
    product_type = factory.SubFactory(ProductTypeFactory)

    @factory.post_generation
    def attribute_value(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.attribute_value.add(*extracted)


# #!AttributeValueFactory
class AttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AttributeValue

    attr_value = "attr_test"
    attribute = factory.SubFactory(AttributeFactory)


# #!ProductLineFactory
class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = "10.00"
    sku = "B700DD1FA82"
    stock_qty = 2
    product = factory.SubFactory(ProductFactory)
    is_active = True
    weight = 100
    product_type = factory.SubFactory(ProductTypeFactory)

    @factory.post_generation
    def attribute_value(self, create, extracted, **kwargs):
        if not create or not extracted:
            return
        self.attribute_value.add(*extracted)


# #!ProductImageFactory
class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    alternative_text = "test alternative text"
    product_image_url = "test.png"
    productline = factory.SubFactory(ProductLineFactory)

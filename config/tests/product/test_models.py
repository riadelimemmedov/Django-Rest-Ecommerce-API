# Django modules and function
from django.core.exceptions import ValidationError

# Pytest
import pytest


# * If you don't declare pytestmark our test class model don't accsess to database table
pytestmark = pytest.mark.django_db


#!TestCategoryModel
class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange

        # Act
        obj = category_factory(name="test_category")

        # Assert
        assert obj.__str__() == "test_category"


#!TestBrandModel
class TestBrandModel:
    def test_str_method(self, brand_factory):
        # Arrange

        # Act
        obj = brand_factory(name="test_brand")

        # Assert
        assert obj.__str__() == "test_brand"


# #!TestProductModel
class TestProductModel:
    def test_str_method(self, product_factory):
        # Arrange

        # Act
        obj = product_factory(name="test_product")

        # Assert
        assert obj.__str__() == "test_product"


#! TestProductLineModel
class TestProductLineModel:
    def test_str_method(self, product_line_factory, attribute_value_factory):
        # Arrange

        # Act
        attr = attribute_value_factory(attr_value="test")
        obj = product_line_factory(sku="10.00", attribute_value=(attr,))

        # Assert
        assert obj.__str__() == "$10.00"

    def test_dublicate_order_value(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            # if create a new object same product value,work pytest.raises(ValidationError) and test pass succsesfully
            product_line_factory(order=1, product=obj).clean()


#!TestProductImageModel
class TestProductImageModel:
    def test_str_method(self, product_image_factory):
        # Arrange

        # Act
        obj = product_image_factory(order=1)

        # Assert
        assert obj.__str__() == "1"


#!TestProductTypeModel
class TestProductTypeModel:
    def test_str_method(self, product_type_factory, attribute_factory):
        # test = attribute_factory(name="test")
        obj = product_type_factory.create(name="test_type")
        assert obj.__str__() == "test_type"


#!TestAttributeModel
class TestAttributeModel:
    def test_str_method(self, attribute_factory):
        obj = attribute_factory(name="test_attribute")
        assert obj.__str__() == "test_attribute"


#!TestAttributeValueModel
class TestAttributeValueModel:
    def test_str_method(self, attribute_value_factory, attribute_factory):
        obj_a = attribute_factory(name="test_attribute")
        obj_b = attribute_value_factory(attr_value="test_value", attribute=obj_a)
        assert obj_b.__str__() == "test_value --- test_attribute"

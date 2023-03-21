# Test Model
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
# class TestProductModel:
#     def test_str_method(self, product_factory):
#         # Arrange

#         # Act
#         obj = product_factory(name="test_product")

#         # Assert
#         assert obj.__str__() == "test_product"

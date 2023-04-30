# Django modules and function
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import transaction

# Models and Serializers
from api.product.models import Category, Product, ProductLine


# Pytest
import pytest


# * If you don't declare pytestmark our test class model don't accsess to database table
pytestmark = pytest.mark.django_db


#!TestCategoryModel
class TestCategoryModel:
    def test_str_method(self, category_factory):
        obj = category_factory(name="test_category")
        assert obj.__str__() == "test_category"

    def test_name_max_length(self, category_factory):
        name = "x" * 230
        slug = "y" * 255
        obj = category_factory(name=name, ctg_slug=slug)
        if len(name) > 235 or len(slug) > 255:
            with pytest.raises(ValidationError) as e:
                obj.full_clean()
        else:
            assert len(name) <= 235
            assert len(slug) <= 255

    def test_name_unique_field(self, category_factory):
        category_factory(name="test_category_name")
        with pytest.raises(IntegrityError) as e:
            category_factory(name="test_category_name")

    def test_ctg_slug_unique_field(self, category_factory):
        category1 = category_factory(name="Category 1", ctg_slug="category")
        try:
            category2 = category_factory(name="Category 2", ctg_slug="category")
        except IntegrityError as e:
            raise e

    def test_is_active_false_default(self, category_factory):
        obj = category_factory()
        assert obj.is_active is False

    def test_parent_category_on_delete_protect(self, category_factory):
        obj = category_factory()
        category_factory(parent=obj)
        with pytest.raises(IntegrityError):
            obj.delete()

    def test_parent_field_null(self, category_factory):
        obj = category_factory()
        assert obj.parent is None

    def test_return_category_active_only_true(self, category_factory):
        category_factory(is_active=True)
        category_factory(is_active=False)
        qs = Category.objects.get_is_active().count()
        assert qs == 1

    def test_return_category_active_only_false(self, category_factory):
        category_factory(is_active=True)
        category_factory(is_active=False)
        qs = Category.objects.count()
        assert qs == 2


#!TestProductModel
class TestProductModel:
    def test_str_method(self, product_factory):
        obj = product_factory(name="test_product")
        assert obj.__str__() == "test_product"

    def test_name_prslug_pid_max_length(self, product_factory):
        name = "x" * 100
        pr_slug = "y" * 255
        pid = "z" * 10
        obj = product_factory(name=name, pr_slug=pr_slug, pid=pid)
        if len(name) > 100 or len(pr_slug) > 255 or len(pid) > 10:
            with pytest.raises(ValidationError) as e:
                obj.full_clean()
        else:
            assert len(name) <= 100
            assert len(pr_slug) <= 255

    def test_is_digital_false_default(self, product_factory):
        obj = product_factory(is_digital=False)
        assert obj.is_digital is False

    def test_fk_category_on_delete_protect(self, category_factory, product_factory):
        obj = category_factory()
        product_factory(category=obj)
        with pytest.raises(IntegrityError):
            obj.delete()

    def test_return_product_active_only_true(self, product_factory):
        product_factory(is_active=True)
        product_factory(is_active=False)
        qs = Product.objects.get_is_active().count()
        assert qs == 1

    def test_return_product_active_only_false(self, product_factory):
        product_factory(is_active=True)
        product_factory(is_active=False)
        qs = Product.objects.all().count()
        assert qs == 2

    def test_fk_product_type_on_delete_protect(
        self, product_type_factory, product_factory
    ):
        obj = product_type_factory()
        product_factory(product_type=obj)
        with pytest.raises(IntegrityError):
            obj.delete()


# #! TestProductLineModel
class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        # Arrange

        # Act
        # attr = attribute_value_factory(attr_value="test")
        obj = product_line_factory(sku="10.00")

        # Assert
        assert obj.__str__() == "$10.00"

    def test_dublicate_order_value(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            # if create a new object same product value,work pytest.raises(ValidationError) and test pass succsesfully
            product_line_factory(order=1, product=obj).clean()

    def test_field_decimal_places(self, product_line_factory):
        price = 1.001
        with pytest.raises(ValidationError):
            product_line_factory(price=price)

    def test_field_max_digits(self, product_line_factory):
        price = 1000.002
        with pytest.raises(ValidationError):
            product_line_factory(price=price)

    def test_field_sku_max_length(self, product_line_factory):
        sku = "x" * 55
        with pytest.raises(ValidationError):
            product_line_factory(sku=sku)

    def test_is_active_false_default(self, product_line_factory):
        obj = product_line_factory(is_active=False)
        assert obj.is_active is False

    def test_fk_product_on_delete_protect(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(product=obj)
        with pytest.raises(IntegrityError):
            obj.delete()

    def test_return_product_line_active_only_true(self, product_line_factory):
        product_line_factory(is_active=True)
        product_line_factory(is_active=False)
        qs = ProductLine.objects.get_is_active().count()
        assert qs == 1

    def test_return_product_line_active_only_false(self, product_line_factory):
        product_line_factory(is_active=True)
        product_line_factory(is_active=False)
        qs = ProductLine.objects.count()
        assert qs == 2

    def test_fk_product_type_on_delete_protect(
        self, product_type_factory, product_line_factory
    ):
        obj = product_type_factory()
        product_line_factory(product_type=obj)
        with pytest.raises(IntegrityError) as e:
            obj.delete()


# #!TestProductImageModel
class TestProductImageModel:
    def test_str_method(self, product_image_factory, product_line_factory):
        # Arrange

        # Act
        productline = product_line_factory(sku="1D0605C019D")
        obj = product_image_factory(order=1, productline=productline)

        # Assert
        assert obj.__str__() == f"{productline.sku}_img"

    @transaction.atomic()
    def test_alternative_text_field_length(self, product_image_factory):
        obj = product_image_factory(alternative_text="This is image")
        with transaction.atomic():
            with pytest.raises(ValidationError) as e:
                obj.full_clean()

    def test_duplicate_order_values(self, product_image_factory, product_line_factory):
        productline = product_line_factory()
        product_image_factory(order=1, productline=productline)
        with pytest.raises(ValidationError):
            product_image_factory(order=1, productline=productline).full_clean()


# #!TestProductTypeModel
class TestProductTypeModel:
    def test_str_method(self, product_type_factory):
        obj = product_type_factory.create(name="test_type")
        assert obj.__str__() == "test_type"

    def test_name_field_max_length(self, product_type_factory):
        name = "x" * 80
        obj = product_type_factory(name=name)
        if len(obj.name) > 100:
            with pytest.raises(ValidationError) as e:
                obj.full_clean()
        else:
            assert len(obj.name) < 100


# #!TestAttributeModel
# class TestAttributeModel:
#     def test_str_method(self, attribute_factory):
#         obj = attribute_factory(name="test_attribute")
#         assert obj.__str__() == "test_attribute"


# #!TestAttributeValueModel
# class TestAttributeValueModel:
#     def test_str_method(self, attribute_value_factory, attribute_factory):
#         obj_a = attribute_factory(name="test_attribute")
#         obj_b = attribute_value_factory(attr_value="test_value", attribute=obj_a)
#         assert obj_b.__str__() == "test_value --- test_attribute"

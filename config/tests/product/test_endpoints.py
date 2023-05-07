# Pytest
import pytest


# Python Modules
import json


# * If you don't declare pytestmark our test class model don't accsess to database table
pytestmark = pytest.mark.django_db


#!TestCategoryEndpoints
class TestCategoryEndpoints:
    endpoint = "/api/category/"

    def test_category_get(self, category_factory, api_client):
        # Arrange

        # create four fake category row for test my category model
        category_factory.create_batch(4)

        # Act
        response = api_client().get(self.endpoint, format="json")

        # Assert
        print("Category content ", json.loads(response.content))

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


# #!TestProductEndpoints
class TestProductEndpoints:
    endpoint = "/api/product/"

    def test_return_all_products(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(
            4
        )  # create four fake product row for test my product model
        # Act
        response = api_client().get(self.endpoint, format="json")
        # Assert
        print("Product content ", json.loads(response.content))

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_return_single_product_by_slug(self, product_factory, api_client):
        obj = product_factory(pr_slug="nike-air-max-90")
        response = api_client().get(f"{self.endpoint}{obj.pr_slug}/", format="json")
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_return_products_by_category_slug(
        self, category_factory, product_factory, api_client
    ):
        obj = category_factory(ctg_slug="shoes")
        product_factory(category=obj)
        response = api_client().get(
            f"{self.endpoint}category/shoes/all/", format="json"
        )
        assert response.status_code == 200

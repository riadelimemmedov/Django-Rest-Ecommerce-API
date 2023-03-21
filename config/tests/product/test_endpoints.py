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
        category_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint, format="json")
        # Assert
        print("Category content ", json.loads(response.content))

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


#!TestBrandEndpoints
class TestBrandEndpoints:
    endpoint = "/api/brand/"

    def test_brand_get(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint, format="json")
        # Assert
        print("Brand content ", json.loads(response.content))

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


#!TestProductEndpoints
class TestProductEndpoints:
    endpoint = "/api/product/"

    def test_product_get(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(4)
        # Act
        response = api_client().get(self.endpoint, format="json")
        # Assert
        print("Product content ", json.loads(response.content))

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

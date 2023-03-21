from pytest_factoryboy import register

from .factories import CategoryFactory, BrandFactory

# if you want call this Factory in the test file you need to declare  bottom_line format = category_factory
register(CategoryFactory)
register(BrandFactory)
# register(ProductFactory)

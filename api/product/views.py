#!Django
from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from django.db import connection

# Django Rest
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets


# Serializers and Models
from .models import *
from .serializers import *
from .fields import *


# Third Party
from drf_spectacular.utils import extend_schema
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import PostgresConsoleLexer
from sqlparse import format

# Create your views here.


#!CategoryView
class CategoryViewSet(viewsets.ViewSet):
    """
    A Viewset for viewing all category
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#!ProductViewSet
class ProductViewSet(viewsets.ViewSet):
    """
    A Viewset for viewing all product
    """

    queryset = Product.objects.get_is_active()
    lookup_field = "slug"

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(responses=ProductSerializer)
    # apple-2022-macbook-pro-laptop-with-m2-chip
    # nike-air-max-90
    # msi-25-speakers-anti-blueflicker-free
    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(
            Product.objects.filter(pr_slug=slug)
            # .select_related("category", "brand") //Because I am delete Brand delete table,If you want keep up this table for this project
            .prefetch_related(Prefetch("products"))
            .prefetch_related(Prefetch("products__product_image"))
            .prefetch_related(Prefetch("products__attribute_value__attribute")),
            many=True,
        )
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # ?Highlet selected query
        # retrieve_product = self.queryset.filter(pr_slug=slug)
        # sqlformatted = format(str(retrieve_product.query), reindent=True)
        # print(
        #     "Result",
        #     highlight(sqlformatted, PostgresConsoleLexer(), TerminalFormatter()),
        # )

        # ?Highliht all queries,when running sql start to render query
        query_list = list(connection.queries)
        print("Length of query list ", len(query_list))

        for q in query_list:
            sqlformatted = format(str(q["sql"]), reindent=True)
            print(
                "Result ",
                highlight(sqlformatted, PostgresConsoleLexer(), TerminalFormatter()),
            )

        return response

    @extend_schema(responses=ProductSerializer)
    @action(
        methods=["GET"],
        detail=False,
        url_path=r"category/(?P<categoryslug>[\w-]+)/all",
        url_name="all",
    )
    def list_product_by_category_slug(self, request, categoryslug=None):
        """
        An endpoint to return products by category
        """
        print("Category Slug Value ", categoryslug)

        serializer = ProductSerializer(
            self.queryset.filter(category__ctg_slug__icontains=categoryslug), many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

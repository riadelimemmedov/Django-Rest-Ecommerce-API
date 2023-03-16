from django.shortcuts import render

#!Django Rest
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets


#!Serializers and Models
from .models import *
from .serializers import *


# Create your views here.


# *CategoryView
class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        print("bunedi hocam ", Category.objects.all())
        return Response(serializer.data, status=status.HTTP_200_OK)

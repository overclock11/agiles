
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.urls import *
from apps.promociones.models import Promotion, Category
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.request import Request

# Serializers define the API representation.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'id')

class CouponSerializer(serializers.HyperlinkedModelSerializer):
    
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Promotion
        fields = ('id', 'name', 'value', 'description', 'image', 'category', 'url')

from django.contrib import admin
from django.urls import path
from apps.promociones.views import index

urlpatterns = [
    path('', index),
]
from django.contrib import admin
from django.urls import path
from apps.promociones.views import *

urlpatterns = [
    path('', index, name='index'),
    path('prueba', prueba, name='prueba'),
    path('<promotion_id>', promotionDetails, name='promotion_details'),
]

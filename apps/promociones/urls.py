from django.contrib import admin
from django.urls import path
from apps.promociones.views import *

urlpatterns = [
    path('', index, name='index'),
    path('<promotion_id>', promotionDetails, name='promotion_details'),
    path('login/signin', loginPage, name='login_page'),
    path('login/request', loginRequest, name='login_request')
]

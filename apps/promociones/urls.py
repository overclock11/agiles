from django.contrib import admin
from django.urls import path
from apps.promociones.views import *

urlpatterns = [
    path('signup', signup, name="signup"),
    path('', index, name='index'),
    path('<promotion_id>', promotionDetails, name='promotion_details'),

]

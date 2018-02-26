"""appAgiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from apps.promociones.admin import admin_site
from django.contrib.auth.urls import *
from apps.promociones.models import Promotion, Category
from apps.promociones.serializers import CategorySerializer, CouponSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework.request import Request

# ViewSets define the view behavior.
class CouponViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = CouponSerializer

    def list(self, request):
        category = request.GET.get('category', 0)
        if (category is 0):
            promotions = Promotion.objects.all()
        else:
            promotions = Promotion.objects.filter(category=category)
        serializer = CouponSerializer(promotions, context={'request': request}, many=True)
        return Response(serializer.data)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'promociones', CouponViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('api/', include(router.urls)),
    path('admin/', admin_site.urls),
    path('promociones/', include('apps.promociones.urls')),
    path('', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

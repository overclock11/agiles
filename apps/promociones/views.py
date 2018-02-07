from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    promotions = Promotion.objects.values()
    return render(request,'promociones/index.html',{'promotions':promotions})

def promotionDetails(request, promotion_id):
    promotion = Promotion.objects.get(id= promotion_id)
    return render(request,'promociones/promotionDetails.html',{'promotion':promotion})    
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

def loginPage(request):
    return render(request, 'promociones/login.html')

def loginRequest(request):
    try:
        user = User.objects.get(user=request.POST['username'])
    except User.DoesNotExist:
        context = { "error_msg": "Invalid user, please try again" }
        return render(request, 'promociones/login.html', context)

    if(user.passw != request.POST['password']):
        context = {"error_msg": "Invalid password, please try again"}
        return render(request, 'promociones/login.html', context)

    # On successfull login...
    request.session["loggedUser"] = user.to_dictionary()
    return index(request)

def logoutRequest(request):
    request.session["loggedUser"] = None
    return index(request)
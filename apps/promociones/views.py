from django.shortcuts import render, redirect
from .forms import AuthUserForm, UserForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction

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

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        auth_form = AuthUserForm(request.POST, instance=request.user)
        user_form = UserForm(request.POST, instance=request.user.user)
        if auth_form.is_valid() and user_form.is_valid():
            print(request.FILES)
            auth_form.save()
            user = user_form.save()
            if 'photo' in request.FILES:
                user.photo = request.FILES['photo']
                user.save()
            messages.success(request, 'Usuario actualizado!')
            return redirect('/admin')
        else:
            messages.error(request, 'Corrija el error..')
    else:
        auth_form = AuthUserForm(instance=request.user)
        print(request.user.user.city)
        user_form = UserForm(instance=request.user.user)
    return render(request, 'user/user.html', {
        'auth_form': auth_form,
        'user_form': user_form
    })
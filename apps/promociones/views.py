from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AuthUserForm, UserForm, CreateUser, UserCreatForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from  datetime import datetime

# Create your views here.
def index(request):
    promotions = Promotion.objects.values()
    return render(request,'promociones/index.html',{'promotions':promotions})

def promotionDetails(request, promotion_id):
    promotion = Promotion.objects.get(id= promotion_id)
    return render(request,'promociones/promotionDetails.html',{'promotion':promotion})

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


def signup(request):
    if request.method == 'POST':
        auth_form = UserCreatForm(request.POST)
        form = CreateUser(request.POST, request.FILES)
        print("iniciando formulario")
        if auth_form.is_valid() and form.is_valid():
            auth_form.staff = True
            auth_form.is_active = True
            auth_form.is_superuser = False
            auth_form.date_joined = datetime.now()
            user_auth =auth_form.instance
            user = form.instance
            user_auth.set_password(user_auth.password)
            user_auth.save()

            user_auth.user.city = user.city
            user_auth.user.address = user.address
            user_auth.user.country = user.country
            user_auth.user.photo = user.photo
            user_auth.user.save()

#            username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('/promociones')
        else:
            print(form.errors.as_data())
            messages.error(request, 'Error de datos' )
    else:
        auth_form = UserCreatForm()
        form = CreateUser()


    return render(request, 'user/signup.html', {
        'auth_form': auth_form,
        'form': form,
    })

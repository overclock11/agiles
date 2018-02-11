from django.shortcuts import render, redirect
from django.http import HttpResponse
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

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        auth_form = AuthUserForm(request.POST, instance=request.user)
        user_form = UserForm(request.POST, instance=request.user.user)
        if auth_form.is_valid() and user_form.is_valid():
            auth_form.save()
            user_form.save()
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


from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from fines.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Sum


def userLogout(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect('index')


def userLogin(request):
    if request.user.is_authenticated and request.user.profile.permission == '1':
        return redirect('drivers')
    elif request.user.is_authenticated and request.user.profile.permission == '3':
        return redirect('driverInfo', id=request.user.id)
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if request.user.profile.permission == '1':
                    return redirect('drivers')
                elif request.user.profile.permission == '3':
                    return redirect('driverInfo', id=request.user.id)
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'index.html', context)

def user_type_redirect(request):
    if request.user.profile.permission == 1:
        return redirect('drivers')
    else:
        return redirect('profile')


@login_required(login_url='index')
def info(request, id):
    info = Profile.objects.get(id=id)
    deviceDetial = DeviceInfo.objects.get(owner=info.id)
    carDetial = CarFineTrack.objects.get(deviceID=deviceDetial.id)
    fineDetial = SpeedTicket.objects.filter(deviceID=deviceDetial.id)
    total = SpeedTicket.objects.filter(deviceID=deviceDetial.id).aggregate(Sum('fine'))
    total1 = total['fine__sum']

    context = {'detail': info, 'device': deviceDetial, 'car': carDetial, 'fines': fineDetial,'total':total1}
    return render(request, 'infoPage.html', context)


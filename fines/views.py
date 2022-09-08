from time import time
from django.shortcuts import render
from django.http import HttpResponse
from .models import SpeedTicket, DeviceInfo
from .serializers import SpeedTicketSerializers, DeviceInfoSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from account.models import Profile
from fines.models import *
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime
from ping3 import ping


def index(request):
    context = {}
    return render(request, 'index.html', context)

## Dashboard
@login_required(login_url='index')
def driversList(request):
    drivers = Profile.objects.filter(permission=3)
    
    final = []
    driverStatus = {}
    driverID = DeviceInfo.objects.values_list('owner','status')
    for st in driverID:
        driverStatus={'id':st[0], 'status':st[1]}
        final.append(driverStatus)
    print(final)
    context = {"drivers":drivers, 'driverID':final}
    
    return render(request, 'drivers.html', context)


@login_required(login_url='index')
def information(request, id):
    userDetail = Profile.objects.get(id=id)
    deviceDetial = DeviceInfo.objects.get(owner=userDetail.id)
    carDetial = CarFineTrack.objects.get(deviceID=deviceDetial.id)
    fineDetial = SpeedTicket.objects.filter(deviceID=deviceDetial.id)
    total = SpeedTicket.objects.filter(deviceID=deviceDetial.id).aggregate(Sum('fine'))
    total1 = total['fine__sum']

    
    context = {'detail':userDetail,'device':deviceDetial,'car':carDetial,'fines':fineDetial,'total':total1}
    return render(request, 'infoPage.html', context)


## API


class DeviceInfoPostAPIView(APIView):

    def post(self, request):
        serializer = DeviceInfoSerializers(data=request.data)
        if serializer.is_valid():
            userT = request.user
            device_ID = DeviceInfo.objects.values_list('deviceID').filter(owner=userT)[0][0]
            devID = DeviceInfo.objects.get(deviceID=device_ID)
            print(serializer.validated_data.get('deviceIP'))
            if devID.deviceIP != serializer.validated_data.get('deviceIP') or None:
                devID.deviceIP = serializer.validated_data.get('deviceIP')
                devID.status = serializer.validated_data.get('status')
                devID.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeedTicketPostAPIView(APIView):

    def post(self, request):
        serializer = SpeedTicketSerializers(data=request.data)
        if serializer.is_valid():
            # token = Token.objects.get(user=userID).key
            userT = request.user
            device_ID = DeviceInfo.objects.values_list('deviceID').filter(owner=userT)[0][0]
            # devID = DeviceInfo.objects.get(deviceID=device_ID).id
            serializer.save(deviceID=DeviceInfo.objects.get(deviceID=device_ID))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def FineInfoDetials(request, id):
#     try:
#         snippet = SpeedTicket.objects.get(id=id)
#     except SpeedTicket.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SpeedTicketSerializers(snippet)
#         userT = request.user.id
#         print(userT)
#         return Response(serializer.data)
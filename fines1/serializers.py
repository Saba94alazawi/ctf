from dataclasses import field
from rest_framework import serializers
from .models import SpeedTicket, DeviceInfo




class SpeedTicketSerializers(serializers.ModelSerializer):
    deviceID = serializers.StringRelatedField()
    class Meta:
        model = SpeedTicket
        fields = '__all__'

class DeviceInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = DeviceInfo
        fields = ['status', 'time']
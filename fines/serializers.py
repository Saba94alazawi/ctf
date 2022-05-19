from rest_framework import serializers
from .models import SpeedTicket




class SpeedTicketSerializers(serializers.ModelSerializer):
    deviceID = serializers.StringRelatedField()
    class Meta:
        model = SpeedTicket
        fields = '__all__'


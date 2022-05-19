from django.db import models
from django.contrib.auth.models import User



class DeviceInfo(models.Model):
    owner = models.ManyToManyField(User)
    deviceID = models.CharField(max_length=36, blank=True, null=False)

    def __str__(self):
        return self.deviceID


class CarFineTrack(models.Model):
    deviceID = models.ForeignKey(DeviceInfo, on_delete=models.CASCADE)
    carBrandName = models.CharField(max_length=50, blank=True, null=False)
    carModelName = models.CharField(max_length=50, blank=True, null=False)
    carColor = models.CharField(max_length=50, blank=True, null=False)
    carModelYear = models.CharField(max_length=4, blank=True, null=False)
    carPlateNumber = models.CharField(max_length=50, blank=True, null=False)
    carGroup = models.CharField(max_length=1, blank=True, null=False)
    carNumber = models.CharField(max_length=15, blank=True, null=False)
    carRegisterd = models.CharField(max_length=50, blank=True, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.carNumber}-{self.carGroup}'


class SpeedTicket(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    deviceID = models.ForeignKey(DeviceInfo, on_delete=models.CASCADE, default=0)
    Latitude = models.CharField(max_length=9, blank=True, null=False)
    Longitude = models.CharField(max_length=9, blank=True, null=False)
    speed = models.PositiveIntegerField(default=0)
    fine = models.PositiveIntegerField(default=55)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.deviceID)


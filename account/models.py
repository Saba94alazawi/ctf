from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from CTF.utils import validate_phone
from rest_framework.authtoken.models import Token


PermissionList=[
    ('1','Admin'),
    ('2','Manager'),
    ('3','Driver')
    ]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='Profile/', verbose_name='Profile Image', blank=True)
    phoneNo = models.CharField(max_length=11, blank=True, null=False, validators=[validate_phone], help_text='077 or 078 or 075')
    permission = models.CharField(max_length=1, choices=PermissionList, default='3')

    def __str__(self):
        return self.user.get_full_name()

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)
    instance.profile.save()
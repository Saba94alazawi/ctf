"""CTF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fines.views import *
from account.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('', userLogin, name='index'),
    path('logout/', userLogout, name='logout'),
    # API
    path('api-auth/', include('rest_framework.urls')),
    path('fine/', SpeedTicketPostAPIView.as_view(), name='fine'),
    # path('info_fine/<int:id>', FineInfoDetials, name='fines'),
    path('api/token', obtain_auth_token, name="auth_token"),
    # dashboard
    path('drivers/', driversList, name='drivers'),
    path('info/<id>', information, name='info'),
    # Account
    path('driver/<id>', info, name='driverInfo' ),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

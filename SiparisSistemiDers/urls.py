"""
URL configuration for SiparisSistemiDers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musteri/', include('apps.musteri.urls')),
    path('adres/', include('apps.adres.urls')),
    path('urun/', include('apps.urun.urls')),
    path('siparis/', include('apps.siparis.urls')),
    path('urun_siparis/', include('apps.urun_siparis.urls')),
    # path('user/', include('apps.user.urls'))
]

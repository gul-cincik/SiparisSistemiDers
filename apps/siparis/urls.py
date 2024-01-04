from django.urls import path
from .views import urun_siparis_olustur

urlpatterns = [
    path('urun_siparis_olustur/', urun_siparis_olustur, name='urun-siparis-olustur'),
]
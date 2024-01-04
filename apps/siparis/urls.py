from django.urls import path
from .views import urun_siparis_olustur, musteri_siparis

urlpatterns = [
    path('urun_siparis_olustur/', urun_siparis_olustur, name='urun-siparis-olustur'),
    path('musteri_siparis/<int:pk>/', musteri_siparis, name='musteri-siparis')
]
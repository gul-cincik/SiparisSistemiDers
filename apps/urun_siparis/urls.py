from django.urls import path
from .views import get_urun_in_siparis, siparis_durumu_guncelle

urlpatterns=[
    path('get_urun_in_siparis', get_urun_in_siparis, name='get-urun-in-siparis'),
    path('siparis_durumu_guncelle', siparis_durumu_guncelle, name='siparis-durumu-guncelle'),
]
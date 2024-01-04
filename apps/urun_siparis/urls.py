from django.urls import path
from .views import get_siparis,siparis_teslimi_guncelle

urlpatterns = [
    path('get_siparis/', get_siparis, name='get-siparis'),
    path('siparis_teslimi_guncelle/', siparis_teslimi_guncelle, name='siparis-teslimi-guncelle'),

]
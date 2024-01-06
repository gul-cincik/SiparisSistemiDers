from rest_framework.routers import DefaultRouter
from .views import AdresViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r'adres', AdresViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('adres/siparis_adresi/', AdresViewSet.as_view({'post': 'siparis_adresi_getir'}), name='siparis-adresi-getir')
]

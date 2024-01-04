from rest_framework.routers import DefaultRouter
from .views import AdresViewSet
from django.urls import path, include
router = DefaultRouter()

router.register(r'adres', AdresViewSet, basename='adres')

urlpatterns = [
    path('', include(router.urls)),
    path('adres/siparisAdresi/', AdresViewSet.as_view({'get': 'siparis_adresi_getir'}), name='siparis_adresi_getir'),

]

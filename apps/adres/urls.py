from rest_framework.routers import DefaultRouter
from .views import AdresViewSet
from django.urls import path, include
router = DefaultRouter()

router.register(r'adres', AdresViewSet)

urlpatterns = [
    path('', include(router.urls))
]

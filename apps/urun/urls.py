from rest_framework.routers import DefaultRouter
from .views import UrunViewSet
from django.urls import path, include
router = DefaultRouter()

router.register(r'urun', UrunViewSet)

urlpatterns = [
    path('', include(router.urls))
]

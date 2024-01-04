from rest_framework import serializers
from .models import Siparis
from apps.urun_siparis.models import UrunSiparis

class SiparisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Siparis
        fields = '__all__'

class UrunSiparisSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrunSiparis
        fields = '__all__'


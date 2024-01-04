from rest_framework import serializers
from .models import UrunSiparis

class UrunSiparisSerializer(serializers.ModelSerializer):

    class Meta:
        model = UrunSiparis
        fields = '__all__'
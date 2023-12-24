from rest_framework import serializers
from .models import Siparis

class SiparisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Siparis
        fields = '__all__'
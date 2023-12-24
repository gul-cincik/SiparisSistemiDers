from rest_framework import serializers
from .models import Adres

class AdresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adres
        fields = '__all__'
from rest_framework import serializers
from .models import Musteri

class MusteriSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musteri
        fields = '__all__'
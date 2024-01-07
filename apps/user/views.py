# user/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
from apps.musteri.models import Musteri  # Make sure to replace 'yourapp' with the actual name of your app

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Extract cinsiyet from request data
            cinsiyet = request.data.get('cinsiyet', '')

            # Create Musteri instance
            musteri = Musteri.objects.create(
                ad=user.first_name,  # Assuming first_name corresponds to 'ad'
                soyad=user.last_name,  # Assuming last_name corresponds to 'soyad'
                cinsiyet=cinsiyet
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

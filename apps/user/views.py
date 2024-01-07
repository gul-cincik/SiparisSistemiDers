from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer

@api_view(['POST'])
def register_user(request):

    serializer = CustomUserSerializer(request.data)

    if serializer.is_valid():
        user = serializer.save()
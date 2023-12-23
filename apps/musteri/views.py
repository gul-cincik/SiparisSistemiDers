from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MusteriSerializer
from .models import Musteri
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class MusteriViewSet(ModelViewSet):
    
    serializer_class = MusteriSerializer
    queryset = Musteri.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):

        try:
            allMusteri = Musteri.objects.all()
            serializer = MusteriSerializer(allMusteri, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        try:
            Musteri = Musteri.objects.get(id=pk)
            serializer = MusteriSerializer(Musteri, many=False)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.siparis.models import Siparis
from .serializers import AdresSerializer
from .models import Adres
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

# Create your views here.

class AdresViewSet(ModelViewSet):
    
    serializer_class = AdresSerializer
    queryset = Adres.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):

        try:
            allAdres = Adres.objects.all()
            serializer = AdresSerializer(allAdres, many=True)
            return Response(serializer.data)
        
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk):
        try:
            Adres = Adres.objects.get(id=pk)
            serializer = AdresSerializer(Adres, many=False)
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
    
    #Musteri ve siparis bazli adres getirme.
    @action(detail=False, methods=['get'], url_path='siparisAdresi')
    def siparis_adresi_getir(self, request):

        try:
            musteri_id = request.query_params.get('musteri_id')
            siparis_id = request.query_params.get('siparis_id')

            if not musteri_id or not siparis_id:
                return Response("musteri_id ve siparis_id gerekli parametreler.", status=status.HTTP_400_BAD_REQUEST)

            siparis = Siparis.objects.filter(musteri__id=musteri_id, id=siparis_id).first()

            if not siparis:
                return Response("Bu müşteriye veya siparişe ait sipariş bilgisi bulunamadı.", status=status.HTTP_404_NOT_FOUND)
            
            adres = Adres.objects.get(id=siparis.adres.id)

            if not adres:
                return Response("Bu müşteriye veya siparişe ait sipariş bilgisi bulunamadı.", status=status.HTTP_404_NOT_FOUND)
            
            serializer = AdresSerializer(adres, many=False)
            return Response(serializer.data)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
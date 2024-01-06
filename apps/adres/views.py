from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AdresSerializer
from .models import Adres
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from apps.musteri.models import Musteri
from apps.siparis.models import Siparis
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
        
    @action(detail=False, methods=['post'], url_path='siparis_adresi')
    def siparis_adresi_getir(self, request):

        #Bu Get methodu kullanıldığında kullanılan kod.
        # musteri_id = request.query_params.get('musteri_id')
        # siparis_id = request.query_params.get('siparis_id')

        musteri_id = request.data['musteri_id']
        siparis_id = request.data['siparis_id']
        if not musteri_id or not siparis_id:

            return Response('Müşteri ve Sipariş id leri zorunlu parametreler.', status=status.HTTP_400_BAD_REQUEST)
        
        musteri = Musteri.objects.get(id=musteri_id)

        if musteri == None:
            return Response('Böyle bir müşteri bulunamadı.', status=status.HTTP_400_BAD_REQUEST)
        
        siparis = Siparis.objects.get(id=siparis_id)

        if siparis == None:
            return Response('Böyle bir müşteri bulunamadı.', status=status.HTTP_400_BAD_REQUEST)
        
        adres = Adres.objects.get(id=siparis.adres.id)

        if adres == None:
            return Response('Bu siparişe ait adres bilgisi girilmemiş.', status=status.HTTP_404_NOT_FOUND)
        
        serializer = AdresSerializer(adres)
        return Response(serializer.data, status=status.HTTP_200_OK)

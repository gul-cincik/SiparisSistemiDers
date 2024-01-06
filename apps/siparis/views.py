from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import Siparis
from apps.urun.models import Urun
from apps.musteri.models import Musteri

from .serializers import SiparisSerializer
from apps.urun_siparis.serializers import UrunSiparisSerializer

@api_view(['POST'])
def urun_siparis_olustur(request):
    urun_detay = request.data.get('urun_detay', [])
    uruns = Urun.objects.filter(id__in=[item['id'] for item in urun_detay])

    if len(uruns) != len(urun_detay):
        return Response({'error': 'Invalid urun_detay provided'}, status=status.HTTP_400_BAD_REQUEST)


    siparis_data = {
        'aciklama': request.data.get('aciklama', ''),
        'adres': request.data.get('adres', None),
        'toplam_fiyat': request.data.get('toplam_fiyat', ''),
        'musteri': request.data.get('musteri', None),
    }
    siparis_serializer = SiparisSerializer(data=siparis_data)

    if siparis_serializer.is_valid():
        siparis = siparis_serializer.save()

        for urun_data in urun_detay:
            urun = Urun.objects.get(id=urun_data['id'])
            urun_siparis_data = {
                'adet': urun_data['adet'],
                'urun': urun.id,
                'siparis': siparis.id,
                'fiyat': urun.fiyat * int(urun_data['adet']),
            }

            urun_siparis_serializer = UrunSiparisSerializer(data=urun_siparis_data)

            if urun_siparis_serializer.is_valid():
                urun_siparis_serializer.save()
            else:
                # Rollback if UrunSiparis creation fails
                siparis.delete()
                return Response({'error': 'UrunSiparis creation failed', 'details': urun_siparis_serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Siparis created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Siparis creation failed', 'details': siparis_serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

#Müşteri bazlı sipariş getirme
@api_view(['GET'])
def musteri_siparis_getir(request,pk):

    musteri = Musteri.objects.get(id=pk)

    if musteri == None:

        return Response({'error': 'Böyle bir müşteri bulunamadı.'}, status=status.HTTP_400_BAD_REQUEST)
    
    siparisler = Siparis.objects.filter(musteri=musteri)

    serialized_siparisler = SiparisSerializer(siparisler, many=True).data

    response_data = {
        'musteri_ad': musteri.ad ,
        'musteri_soyad' : musteri.soyad,
        'siparisler': serialized_siparisler
    }

    return Response(response_data, status=status.HTTP_200_OK)
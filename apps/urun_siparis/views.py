from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection

from apps.musteri.models import Musteri
from apps.siparis.models import Siparis
from .models import UrunSiparis
from .serializers import UrunSiparisSerializer

@api_view(['POST'])
def get_urun_in_siparis(request):

    try:
        musteri_id = request.data['musteri_id']
        siparis_id = request.data['siparis_id']
        
        musteri = Musteri.objects.get(id=musteri_id)

        if musteri == None:

            return Response('Böyle bir müşteri bulunamadı.', status=status.HTTP_404_NOT_FOUND)
        
        siparis = Siparis.objects.get(id=siparis_id)

        if siparis==None:
            return Response('Böyle bir siparis bulunamadı.', status=status.HTTP_404_NOT_FOUND)
        
        raw_query = '''
            SELECT m.ad AS musteri_ad,
                    m.soyad AS musteri_soyad,
                    u.marka AS marka,
                    u.aciklama AS urun_aciklama,
                    us.adet AS urun_adet,
                    s.created_at AS siparis_tarihi
            FROM urun_siparis us 
            INNER JOIN urun u ON us.urun_id = u.id 
            INNER JOIN siparis s ON us.siparis_id = s.id 
            INNER JOIN musteri m ON s.musteri_id = m.id 
            WHERE m.id = %s AND s.id = %s 
            AND s.is_deleted = FALSE AND m.is_deleted = FALSE  AND us.is_deleted = FALSE 
            AND u.is_deleted = FALSE 
            AND us.siparis_durumu = 0
        '''

        with connection.cursor() as cursor:
            cursor.execute(raw_query, [musteri_id, siparis_id])
            results = cursor.fetchall()
        

        formatted_results = [
            {
                'ad': row[0],
                'soyad': row[1],
                'marka': row[2],
                'aciklama': row[3],
                'adet': row[4],
                'siparis_tarihi': row[5]
            } for row in results
        ]

        sonuclar = {'Kullanıcı ve sipariş bazlı ürün listesi': formatted_results}

        return Response(sonuclar, status=status.HTTP_200_OK)

    except Exception as e:

        return Response(f'Error! {e}', status=status.HTTP_400_BAD_REQUEST)        
    
@api_view(['PUT'])
def siparis_durumu_guncelle(request):

    try:

        if 'urunsiparis_id' not in request.data:

            return Response('urunsiparis_id gerekli alan.', status=status.HTTP_400_BAD_REQUEST)
        
        urunsiparis_id = request.data['urunsiparis_id']

        urunsiparis = UrunSiparis.objects.get(id=urunsiparis_id)

        if 'siparis_durumu' not in request.data:

            return Response('siparis_durumu gerekli alan', status=status.HTTP_400_BAD_REQUEST)
        
        urunsiparis.siparis_durumu = request.data['siparis_durumu']

        urunsiparis.save()

        serializer = UrunSiparisSerializer(urunsiparis)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except UrunSiparis.DoesNotExist:

        return Response('Böyle bir ürün bulunamadı', status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response(f'ERROR!, {e}', status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Siparis
from .serializers import UrunSiparisSerializer
from apps.urun.models import Urun
from apps.musteri.models import Musteri
from .models import UrunSiparis
from django.db import connection

@api_view(['POST'])
def get_siparis(request):

    musteri = Musteri.objects.get(id=request.data['musteri_id'])

    if musteri==None:

        return Response({'error': 'Böyle bir müşteri bulunamadı.'})
    
    siparis = Siparis.objects.get(id=request.data['siparis_id'])

    if(siparis.musteri.id != musteri.id):

        return Response({'error': 'Bu müşteriye ait böyle bir sipariş bulunamadı.'})
    
    raw_query = '''
        SELECT u.marka, 
            u.aciklama AS urun_aciklama, 
            us.adet, 
            m.ad,
            m.soyad,
            us.created_at AS siparis_tarihi
        FROM urun_siparis us 
        INNER JOIN urun u ON us.urun_id = u.id 
        INNER JOIN siparis s ON us.siparis_id = s.id 
        INNER JOIN musteri m ON s.musteri_id = m.id 
        WHERE u.is_deleted = FALSE AND us.is_deleted = FALSE AND m.is_deleted = FALSE AND us.siparis_durumu=0
        AND m.id = %s AND s.id = %s

    '''

    with connection.cursor() as cursor:
        cursor.execute(raw_query, [request.data['musteri_id'], request.data['siparis_id']])
        results = cursor.fetchall()

    formatted_results = [{'marka': row[0], 'urun_aciklama': row[1], 'adet': row[2], 'ad': row[3], 'soyad': row[4], 'siparis_tarihi': row[5]} for row in results]

    combined_results = {'Kulanıcı bazlı ürün sipariş listesi': formatted_results}

    return Response(combined_results)


@api_view(['PUT'])
def siparis_teslimi_guncelle(request):
    try:
        if 'urunsiparis_id' not in request.data:
            return Response("'urunsiparis_id' gerekli alan.", status=status.HTTP_400_BAD_REQUEST)

        urunsiparis_id = request.data['urunsiparis_id']

        urun_siparis = UrunSiparis.objects.get(id=urunsiparis_id)

        if 'siparis_durumu' not in request.data:
            return Response("'siparis_durumu' gerekli alan.", status=status.HTTP_400_BAD_REQUEST)

        urun_siparis.siparis_durumu = request.data['siparis_durumu']

        urun_siparis.save()

        serializer = UrunSiparisSerializer(urun_siparis)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except UrunSiparis.DoesNotExist:
        return Response(f"UrunSiparis with id {urunsiparis_id} does not exist.", status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

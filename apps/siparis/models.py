from django.db import models
from datetime import datetime
from apps.adres.models import Adres
from apps.musteri.models import Musteri

class Siparis(models.Model):
    class Meta:
        db_table = 'siparis'


    id = models.AutoField(primary_key=True)
    aciklama = models.TextField()
    adres_id = models.ForeignKey(Adres, on_delete=models.DO_NOTHING)
    toplam_fiyat = models.FloatField(null=False, default= 0)
    musteri_id = models.ForeignKey(Musteri, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, editable= False)
    is_deleted = models.BooleanField(default = False)
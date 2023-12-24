from django.db import models
from datetime import datetime
from apps.musteri.models import Musteri



class Adres(models.Model):
    class Meta:
        db_table = 'adres'

    id = models.AutoField(primary_key=True)
    sehir = models.CharField(max_length=255)
    ilce = models.CharField(max_length=255)
    aciklama = models.TextField()
    musteri = models.ForeignKey(Musteri, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=datetime.now, editable= False)
    is_deleted = models.BooleanField(default = False)
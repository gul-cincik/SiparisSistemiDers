from django.db import models
from datetime import datetime
# Create your models here.

class Musteri(models.Model):

    class Meta:
        db_table='musteri'

    id = models.AutoField(primary_key=True)
    ad = models.CharField(max_length=255, null=False)
    soyad = models.CharField(max_length=255, null=False)
    cinsiyet = models.CharField(max_length=255)

    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    is_deleted = models.BooleanField(default=False)

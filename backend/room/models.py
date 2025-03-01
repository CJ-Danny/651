from django.db import models


# Create your models here.
class Room(models.Model):
    roomId = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255)
    name = models.CharField(max_length=30, default='')
    imgUrl = models.CharField(max_length=300, default='')
    floor = models.CharField(max_length=30, default='1')
    price = models.IntegerField(default=0)
    area = models.CharField(max_length=30, default='0')
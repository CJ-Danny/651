from django.db import models


# Create your models here.
class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    userID = models.IntegerField(default=-1)
    roomID = models.IntegerField(default=-1)
    submitTime = models.DateTimeField(default='2000-01-01 00:00')
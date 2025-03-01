from django.db import models


# Create your models here.
class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    userID = models.IntegerField(default=-1)
    roomID = models.IntegerField(default=-1)
    status = models.IntegerField(default=0)  # 0 not distribute, 1 don't finish, 2 finish, 3 error
    submitTime = models.DateTimeField(default='2000-01-01 00:00')
    description = models.CharField(max_length=100, default='')
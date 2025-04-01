from django.db import models


# Create your models here.
class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    userID = models.IntegerField(default=-1)
    roomID = models.IntegerField(default=-1)
    description = models.CharField(max_length=500, default='')
    submitTime = models.DateTimeField(null=True)
    status = models.IntegerField(default=0)  # 0 not distribute, 1 don't finish, 2 finish, 3 error

    managerID = models.IntegerField(default=-1)
    assignTime = models.DateTimeField(null=True)

    finishTime = models.DateTimeField(null=True)
    method = models.CharField(max_length=500, default='')
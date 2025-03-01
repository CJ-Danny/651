from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    type = models.IntegerField(null=True)  # 0 means normal user, 1 means invitor
    email = models.CharField(max_length=30, default="")


class Rent(models.Model):
    rentId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    roomId = models.CharField(max_length=255)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    applyTime = models.DateTimeField()


class Bill(models.Model):
    billId = models.AutoField(primary_key=True)
    rentID = models.IntegerField()


class RegisterCode(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30, default="")
    code = models.CharField(max_length=30, default="")
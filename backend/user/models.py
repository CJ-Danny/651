from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default="")


class Rent(models.Model):
    rentId = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    roomId = models.IntegerField(default=0)
    status = models.IntegerField(default=0)  # 0 pending approve, 1 approved, 2 reject
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    applyTime = models.DateTimeField()


class Bill(models.Model):
    billId = models.AutoField(primary_key=True)
    rentID = models.IntegerField()
    status = models.IntegerField(default=0)  # 0 unpaid, 1 payed
    createTime = models.DateTimeField()
    due = models.DateTimeField()
    money = models.IntegerField(default=0)


class RegisterCode(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=30, default="")
    code = models.CharField(max_length=30, default="")
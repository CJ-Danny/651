from django.db import models


# Create your models here.
class Manager(models.Model):
    managerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default="")
    type = models.IntegerField()  # 1~4 admain、water、electric、machine
    status = models.IntegerField()  # 0 busy, 1 can be selected


class Knowledge(models.Model):
    knowledgeId = models.AutoField(primary_key=True)
    problem = models.CharField(max_length=100)
    solution = models.TextField(max_length=2000)
    type = models.IntegerField(default=0)

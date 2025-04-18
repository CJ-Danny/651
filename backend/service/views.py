import datetime

from django.shortcuts import render
import string
import random

from django.core import mail
from django.core.mail import EmailMultiAlternatives, send_mail
from django.forms import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
from backend import settings
from backend.settings import EMAIL_HOST_USER
from room.models import *
from service.models import *
from user.models import *
from manager.models import *
from user.token import *


# Create your views here.
@csrf_exempt
def getAllOrders(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    orders = list(Order.objects.all().values())
    for order in orders:
        room = Room.objects.get(roomId=order['roomID'])
        order['roomNumber'] = room.number
    return JsonResponse({'errno': 0, 'data': orders})


@csrf_exempt
def assainOrder(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    orderID = str(request.POST.get('orderID'))
    managerID = str(request.POST.get('managerID'))
    order = Order.objects.get(orderID=orderID)
    order.managerID = managerID
    order.status = 1
    order.assignTime = datetime.datetime.now()
    order.save()
    return JsonResponse({'errno': 0, 'msg': "success"})


@csrf_exempt
def getManagerOrder(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    managerID = str(request.POST.get('managerID'))
    orders = list(Order.objects.filter(managerID=managerID).values())
    for order in orders:
        room = Room.objects.get(roomId=order['roomID'])
        order['roomNumber'] = room.number
    return JsonResponse({'errno': 0, 'data': orders})


@csrf_exempt
def finishOrder(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    orderID = str(request.POST.get('orderID'))
    method = request.POST.get('method')
    order = Order.objects.get(orderID=orderID)
    order.status = 2
    order.method = method
    order.finishTime = datetime.datetime.now()
    order.save()
    return JsonResponse({'errno': 0, 'msg': "success"})
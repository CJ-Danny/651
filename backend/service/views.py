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
    return JsonResponse({'errno': 0, 'data': orders})

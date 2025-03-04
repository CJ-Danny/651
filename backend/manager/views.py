from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from room.models import *
from service.models import *
from user.models import *
from manager.models import *
from user.token import *


# Create your views here.
@csrf_exempt
def getRentInfo(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    status = request.POST.get('status', -1)
    if status == -1:
        rents = Rent.objects.all().order_by("-applyTime")
    else:
        rents = Rent.objects.filter(status=status).order_by("-applyTime")
    rents = list(rents.values())
    for rent in rents:
        if rent['status'] == 0:
            rent['status'] = 'pending review'
        elif rent['status'] == 1:
            rent['status'] = 'approved'
        else:
            rent['status'] = 'terminal'
    return JsonResponse({'errno': 0, 'data': rents})


@csrf_exempt
def reviewRent(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    rentId = request.POST.get('rentId')
    status = request.POST.get('status')
    rent = Rent.objects.get(rentId=rentId)
    rent.status = status
    rent.save()
    return JsonResponse({'errno': 0, 'msg': "review success"})

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


@csrf_exempt
def getUserInfo(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})

    data = []
    users = User.objects.all()

    for user in users:
        rents = Rent.objects.filter(userId=user.userId)
        bill_unpaid_num = 0
        rent_num = rents.count()

        for rent in rents:
            bill_unpaid_num += Bill.objects.filter(rentID=rent.rentId, status=0).count()

        data.append({
            'userId': user.userId,
            'userName': user.userName,
            'email': user.email,
            'rent_num': rent_num,
            'bill_unpaid_num': bill_unpaid_num
        })
    return JsonResponse({'errno': 0, 'data': data})


@csrf_exempt
def getManagerInfo(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})

    data = []
    managers = Manager.objects.exclude(type=1)

    for manager in managers:
        finished_num = Order.objects.filter(managerID=manager.managerId, status=2).count()
        unfinished_num = Order.objects.filter(managerID=manager.managerId, status=1).count()

        data.append({
            'managerId': manager.managerId,
            'name': manager.name,
            'email': manager.email,
            'type': manager.type,
            'status': manager.status,
            'finished_num': finished_num,
            'unfinished_num': unfinished_num
        })

    return JsonResponse({'errno': 0, 'data': data})
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from room.models import *
from service.models import *
from user.models import *
from manager.models import *
from user.token import *


# Create your views here.
@csrf_exempt
def getRoomsInfo(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    rooms = Room.objects.all()
    data = []
    for room in rooms:
        # curTime = datetime.datetime.now()
        rents = Rent.objects.filter(roomId=room.roomId).filter(status=1)
            # .filter(startTime__lt=curTime).filter(endTime__gt=curTime)

        if rents.exists():
            rent = rents.first()
            user = User.objects.get(userId=rent.userId)
            roomStatus = 1  # rent

            repairOrders = Order.objects.filter(roomID=room.roomId) \
                .filter(Q(status=1) | Q(status=0))
            bills = Bill.objects.filter(rentID=rent.rentId).filter(status=0)
            if repairOrders.exists():  # rent and repair
                roomStatus = 3
                if bills.exists():  # rent and repair and overdue
                    roomStatus = 23
            elif bills.exists():  # rent and overdue
                roomStatus = 2

            data.append({
                'roomID': room.roomId,
                'roomNumber': room.number,
                'roomName': room.name,
                'imgUrl': room.imgUrl,
                'floor': room.floor,
                'price': room.price,
                'area': room.area,
                'status': roomStatus,
                'startTime': rent.startTime.strftime('%Y-%m-%d %H:%M'),
                'endTime': rent.endTime.strftime('%Y-%m-%d %H:%M'),
                'userID': rent.userId,
                'rentID': rent.rentId,
                'userName': user.userName,
            })
        else:
            data.append({
                'roomID': room.roomId,
                'roomNumber': room.number,
                'roomName': room.name,
                'imgUrl': room.imgUrl,
                'floor': room.floor,
                'price': room.price,
                'area': room.area,
                'status': 0,  # no rent
                'startTime': '',
                'endTime': '',
                'userID': '',
                'rentID': '',
                'userName': '',
            })
    return JsonResponse({'data': data})

@csrf_exempt
def getBills(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    rentID = request.POST.get('rentID')
    bills = list(Bill.objects.filter(rentID=rentID).values())
    return JsonResponse({'errno': 0, 'msg': "success", 'bills': bills})


@csrf_exempt
def createBill(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})

    rentID = request.POST.get('rentID')
    due_date_str = request.POST.get('due')
    money = request.POST.get('money', 0)

    if not rentID or not due_date_str:
        return JsonResponse({'errno': 1001, 'msg': "missing rentID or due date"})

    try:
        due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d')
    except ValueError:
        return JsonResponse({'errno': 1002, 'msg': "invalid due date format, expected 'YYYY-MM-DD'"})

    bill = Bill(
        rentID=rentID,
        createTime=datetime.datetime.now(),
        due=due_date,
        money=money
    )
    bill.save()

    return JsonResponse({'errno': 0, 'msg': "bill created successfully"})


@csrf_exempt
def payBill(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    billID = request.POST.get('billID')
    status = request.POST.get('status')
    bill = Bill.objects.get(billId=billID)
    bill.status = status
    bill.save()
    return JsonResponse({'errno': 0, 'msg': "success"})
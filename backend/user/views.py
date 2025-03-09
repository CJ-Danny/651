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


@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    email = str(request.POST.get('email'))
    password = str(request.POST.get('password'))
    type = int(request.POST.get('type'))
    if type == 0 and not User.objects.filter(email=email).exists():
        return JsonResponse({'errno': 1000, 'msg': "user do not exist"})
    elif type == 1 and not Manager.objects.filter(email=email).exists():
        return JsonResponse({'errno': 1000, 'msg': "manager do not exist"})
    else:
        if type == 0:
            user = User.objects.get(email=email)
            if user.password != password:
                return JsonResponse({'errno': 1000, 'msg': "password wrong!"})
            token = GetToken(email, user.userId)
            token = str(token)
            token = token[1:]
            request.session["token"] = token
            return JsonResponse({'errno': 0, 'msg': "登录成功", 'token': token})
        else:
            manager = Manager.objects.get(email=email)
            if manager.password != password:
                return JsonResponse({'errno': 1000, 'msg': "password wrong!"})
            token = GetToken(email, manager.managerId)
            token = str(token)
            token = token[1:]
            request.session["token"] = token
            return JsonResponse({'errno': 0, 'msg': "login success",
                                 'token': token,
                                 'type': manager.type,
                                 'id': manager.managerId
                                 })


def generate_verification_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def send_verification_email(email, verification_code):
    subject = '[Registration Code]'
    html_content = '''
    <p>Your registration code is:</p>
    <h2>{}</h2>
    <p>Please use this code to complete your registration. The code is valid for 30 minutes.</p>
    '''.format(verification_code)
    text_content = 'Your registration code is: {}'.format(verification_code)
    mail.send_mail(
        subject=subject,
        message=text_content,
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=html_content
    )


@csrf_exempt
def registerEmail(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    email = str(request.POST.get('email'))
    if User.objects.filter(email=email).exists():
        return JsonResponse({'errno': 1000, 'msg': "email already register"})
    else:
        verification_code = generate_verification_code()
        if RegisterCode.objects.filter(email=email):
            registerCode = RegisterCode.objects.get(email=email)
        else:
            registerCode = RegisterCode(email=email)
        registerCode.code = verification_code
        registerCode.save()
        send_verification_email(email, verification_code)
        return JsonResponse({'errno': 0, 'msg': "email send success"})


@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    userName = str(request.POST.get('userName'))
    password = str(request.POST.get('password'))
    code = str(request.POST.get('code'))
    email = str(request.POST.get('email'))
    if not RegisterCode.objects.filter(email=email, code=code).exists():
        return JsonResponse({'errno': 1000, 'msg': "code error!"})
    elif User.objects.filter(email=email).exists():
        return JsonResponse({'errno': 1000, 'msg': "user exists"})
    else:
        user = User(
            userName=userName,
            password=password,
            email=email
        )
        user.save()
        RegisterCode.objects.filter(email=email, code=code).delete()
        return JsonResponse({'errno': 0, 'msg': "register success"})


@csrf_exempt
def getHomeInfo(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    token = request.POST.get('token')
    userID, type = Check(token)
    try:
        user = User.objects.get(userId=userID)
    except:
        return JsonResponse({'errno': 1002, 'msg': 'token error'})
    rents = list(Rent.objects.filter(userId=userID).order_by('-applyTime').values())
    for rent in rents:
        room = Room.objects.get(roomId=rent['roomId'])
        rent['roomNumber'] = room.number
        rent['roomId'] = room.roomId
    data = {
        'userName': user.userName,
        'email': user.email,
        'userID': user.userId,
        'rentList': rents
    }
    return JsonResponse({'errno': 0, 'data': data})


@csrf_exempt
def getRentInfo(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    rentId = request.POST.get('rentId')
    rent = Rent.objects.get(rentId=rentId)
    bills = list(Bill.objects.filter(rentID=rentId).values())
    room = Room.objects.get(roomId=rent.roomId)

    data = {
        "rent": model_to_dict(rent),
        "bills": bills,
        "room": model_to_dict(room)
    }
    return JsonResponse({'errno': 0, 'data': data})


@csrf_exempt
def applyRoom(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    token = request.POST.get('token')
    roomId = request.POST.get('roomId')
    startTime = request.POST.get('startTime')
    endTime = request.POST.get('endTime')
    userID, _ = Check(token)
    try:
        user = User.objects.get(userId=userID)
    except:
        return JsonResponse({'errno': 1002, 'msg': 'token error'})
    rent = Rent(
        userId=user.userId,
        roomId=roomId,
        status=0,
        startTime=startTime,
        endTime=endTime,
        applyTime=datetime.datetime.now()
    )
    rent.save()
    return JsonResponse({'errno': 0, 'msg': "apply success"})


@csrf_exempt
def getOrders(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    token = request.POST.get('token')
    userID, type = Check(token)
    try:
        user = User.objects.get(userId=userID)
    except:
        return JsonResponse({'errno': 1002, 'msg': 'token error'})
    orders = list(Order.objects.filter(userID=user.userId).values())
    return JsonResponse({'errno': 0, 'data': orders})


@csrf_exempt
def applyOrder(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "wrong method"})
    token = request.POST.get('token')
    roomId = request.POST.get('roomId')
    description = request.POST.get('description')
    userID, type = Check(token)
    try:
        user = User.objects.get(userId=userID)
    except:
        return JsonResponse({'errno': 1002, 'msg': 'token error'})
    order = Order(
        userID=user.userId,
        roomID=roomId,
        status=0,
        description=description,
        submitTime=datetime.datetime.now()
    )
    order.save()
    return JsonResponse({'errno': 0, 'msg': "apply success"})
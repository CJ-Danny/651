from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
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
            token = GetToken(email, user.userId, user.type)
            token = str(token)
            token = token[1:]
            request.session["token"] = token
            return JsonResponse({'errno': 0, 'msg': "登录成功",
                                 'token': token,
                                 'type': user.type})
        else:
            manager = Manager.objects.get(email=email)
            if manager.password != password:
                return JsonResponse({'errno': 1000, 'msg': "password wrong!"})
            token = GetToken(email, manager.managerId, manager.type)
            token = str(token)
            token = token[1:]
            request.session["token"] = token
            return JsonResponse({'errno': 0, 'msg': "登录成功",
                                 'token': token,
                                 'type': manager.type,
                                 'id': manager.managerId
                                 })
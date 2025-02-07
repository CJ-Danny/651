from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def helloworld(request):
    if request.method != 'POST':
        return JsonResponse({'errno': 1000, 'msg': "请求方法错误"})
    return JsonResponse({'errno': 0, 'msg': "hello",})
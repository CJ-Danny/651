from django.urls import path
from .views import *

urlpatterns = [
    path('getRoomsInfo', getRoomsInfo, name='getRoomsInfo'),
    path('createBill', createBill, name='createBill'),
    path('getBills', getBills, name='getBills'),
    path('payBill', payBill, name='payBill'),
]
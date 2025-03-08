from django.urls import path
from .views import *

urlpatterns = [
    path('getRoomsInfo', getRoomsInfo, name='getRoomsInfo'),
    path('createBill', createBill, name='createBill')
]
from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('registerEmail', registerEmail, name='registerEmail'),
    path('register', register, name='register'),
    path('getHomeInfo', getHomeInfo, name='getHomeInfo'),
    path('getRentInfo', getRentInfo, name='getRentInfo'),
    path('applyRoom', applyRoom, name='applyRoom'),
    path('getOrders', getOrders, name='getOrders'),
    path('applyOrder', applyOrder, name='applyOrder'),
]
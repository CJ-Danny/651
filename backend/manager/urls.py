from django.urls import path
from .views import *

urlpatterns = [
    path('getRentInfo', getRentInfo, name='getRentInfo'),
    path('reviewRent', reviewRent, name='reviewRent'),
    path('getUserInfo', getUserInfo, name='getUserInfo'),
    path('getManagerInfo', getManagerInfo, name='getManagerInfo'),
]
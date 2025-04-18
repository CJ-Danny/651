from django.urls import path
from .views import *

urlpatterns = [
    path('ManagerGetRentInfo', ManagerGetRentInfo, name='ManagerGetRentInfo'),
    path('reviewRent', reviewRent, name='reviewRent'),
    path('getUserInfo', getUserInfo, name='getUserInfo'),
    path('getManagerInfo', getManagerInfo, name='getManagerInfo'),
    path('addManager', addManager, name='addManager'),
    path('deleteManager', deleteManager, name='deleteManager'),
    path('getAllKnowledge', getAllKnowledge, name='getAllKnowledge'),
    path('addKnowledge', addKnowledge, name='addKnowledge'),
    path('searchKnowledge', searchKnowledge, name='searchKnowledge'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('login', login),
    path('registerEmail', registerEmail),
    path('register', register),
    path('getHomeInfo', getHomeInfo),
    path('getRentInfo', getRentInfo),
    path('applyRoom', applyRoom),
    path('applyOrder', applyOrder),
]
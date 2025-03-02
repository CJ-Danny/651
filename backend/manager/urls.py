from django.urls import path
from .views import *

urlpatterns = [
    path('getRentInfo', getRentInfo),
    path('reviewRent', reviewRent),
]
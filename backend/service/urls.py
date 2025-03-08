from django.urls import path
from .views import *

urlpatterns = [
    path('getAllOrders', getAllOrders, name='getAllOrders'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('getAllOrders', getAllOrders, name='getAllOrders'),
    path('assainOrder', assainOrder, name='assainOrder'),
    path('getManagerOrder', getManagerOrder, name='getManagerOrder'),
    path('finishOrder', finishOrder, name='finishOrder'),
]
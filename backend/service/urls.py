from django.urls import path
from .views import *

urlpatterns = [
    path('getAllOrders', getAllOrders, name='getAllOrders'),
    path('assainOrder', assainOrder, name='assainOrder'),
    path('finishOrder', finishOrder, name='finishOrder'),
]
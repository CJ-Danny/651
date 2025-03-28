import datetime

from manager.models import *
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from room.models import *
from .models import *
from user.token import *
from user.models import *
from service.models import *


class GetAllOrdersTest(TestCase):
    def setUp(self):
        self.client = self.client_class()

        self.user = User.objects.create(
            userId=123,
            userName="danny",
            password="test",
            email="test@gmail.com"
        )

        self.order1 = Order.objects.create(
            userID=self.user.userId,
            roomID=101,
            description="Order 1 description",
            submitTime=timezone.now(),
            assignTime=timezone.now(),
            finishTime=timezone.now(),
            status=0
        )
        self.order2 = Order.objects.create(
            userID=self.user.userId,
            roomID=102,
            description="Order 2 description",
            submitTime=timezone.now(),
            assignTime=timezone.now(),
            finishTime=timezone.now(),
            status=1
        )

    def test_get_all_orders_success(self):
        response = self.client.post(reverse('getAllOrders'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)

        data = response.json()['data']
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['roomID'], self.order1.roomID)
        self.assertEqual(data[1]['roomID'], self.order2.roomID)

    def test_get_all_orders_wrong_method(self):
        response = self.client.get(reverse('getAllOrders'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")


class AssainOrderTest(TestCase):
    def setUp(self):
        self.client = self.client_class()

        self.user = User.objects.create(
            userId=123,
            userName="danny",
            password="test",
            email="test@gmail.com"
        )

        self.order = Order.objects.create(
            userID=self.user.userId,
            roomID=101,
            description="Order description",
            submitTime=timezone.now(),
            assignTime=timezone.now(),
            finishTime=timezone.now(),
            status=0
        )

    def test_assain_order_success(self):
        response = self.client.post(reverse('assainOrder'), {
            'orderID': self.order.orderID,
            'managerID': 999
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)
        self.assertEqual(response.json()['msg'], "success")

        self.order.refresh_from_db()
        self.assertEqual(self.order.managerID, 999)
        self.assertEqual(self.order.status, 1)

    def test_assain_order_wrong_method(self):
        response = self.client.get(reverse('assainOrder'), {
            'orderID': self.order.orderID,
            'managerID': 999
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")
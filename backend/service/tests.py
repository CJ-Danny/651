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


class GetManagerOrderTest(TestCase):
    def setUp(self):
        self.client = self.client_class()

        self.manager = User.objects.create(
            userId=456,
            userName="manager",
            password="test",
            email="manager@gmail.com"
        )

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
            status=1,
            managerID=self.manager.userId
        )

        self.order2 = Order.objects.create(
            userID=self.user.userId,
            roomID=102,
            description="Order 2 description",
            submitTime=timezone.now(),
            assignTime=timezone.now(),
            finishTime=timezone.now(),
            status=1,
            managerID=self.manager.userId
        )

        self.order3 = Order.objects.create(
            userID=self.user.userId,
            roomID=103,
            description="Order 3 description",
            submitTime=timezone.now(),
            assignTime=timezone.now(),
            finishTime=timezone.now(),
            status=0,
            managerID=self.user.userId
        )

    def test_get_manager_orders_success(self):
        response = self.client.post(reverse('getManagerOrder'), {
            'managerID': self.manager.userId
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)
        self.assertEqual(len(response.json()['data']), 2)

        order_ids = [order['orderID'] for order in response.json()['data']]
        self.assertIn(self.order1.orderID, order_ids)
        self.assertIn(self.order2.orderID, order_ids)

    def test_get_manager_orders_wrong_method(self):
        response = self.client.get(reverse('getManagerOrder'), {
            'managerID': self.manager.userId
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")

    def test_get_manager_orders_no_orders(self):
        response = self.client.post(reverse('getManagerOrder'), {
            'managerID': 9999
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)
        self.assertEqual(response.json()['data'], [])


class FinishOrderTest(TestCase):
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
            status=1,
            managerID=456,
        )

    def test_finish_order_success(self):
        response = self.client.post(reverse('finishOrder'), {
            'orderID': self.order.orderID,
            'method': 'Credit Card'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)
        self.assertEqual(response.json()['msg'], "success")

        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 2)
        self.assertEqual(self.order.method, 'Credit Card')
        self.assertTrue(self.order.finishTime)

    def test_finish_order_wrong_method(self):
        response = self.client.get(reverse('finishOrder'), {
            'orderID': self.order.orderID,
            'method': 'Credit Card'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")
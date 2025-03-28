from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from user.models import *
from service.models import *
from room.models import *

class ManagerGetRentInfoTest(TestCase):
    def setUp(self):
        self.client = self.client_class()

        self.user = User.objects.create(
            userId=123,
            userName="danny",
            password="test",
            email="test@gmail.com"
        )

        self.rent1 = Rent.objects.create(
            rentId=1,
            userId=self.user.userId,
            roomId=1,
            status=0,
            startTime=timezone.now() - timezone.timedelta(days=10),
            endTime=timezone.now() + timezone.timedelta(days=20),
            applyTime=timezone.now() - timezone.timedelta(days=15)
        )

        self.rent2 = Rent.objects.create(
            rentId=2,
            userId=self.user.userId,
            roomId=2,
            status=1,
            startTime=timezone.now() - timezone.timedelta(days=5),
            endTime=timezone.now() + timezone.timedelta(days=25),
            applyTime=timezone.now() - timezone.timedelta(days=7)
        )

    def test_manager_get_rent_info_all_status(self):
        response = self.client.post(reverse('ManagerGetRentInfo'), {
            'status': -1
        })

        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        self.assertEqual(response_data['errno'], 0)

    def test_manager_get_rent_info_filtered_by_status(self):
        response = self.client.post(reverse('ManagerGetRentInfo'), {
            'status': 1
        })

        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        self.assertEqual(response_data['errno'], 0)
        self.assertEqual(len(response_data['data']), 1)

        rent = response_data['data'][0]
        self.assertEqual(rent['status'], 'approved')
        self.assertEqual(rent['rentId'], 2)

    def test_manager_get_rent_info_invalid_method(self):
        # 使用 GET 请求而不是 POST
        response = self.client.get(reverse('ManagerGetRentInfo'), {
            'status': 1
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")

    def test_manager_get_rent_info_no_status_param(self):
        # 不提供 status 参数，默认为 -1 (查询所有)
        response = self.client.post(reverse('ManagerGetRentInfo'))

        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        self.assertEqual(response_data['errno'], 0)
        self.assertEqual(len(response_data['data']), 2)  # 需要返回所有租赁记录

    def test_manager_get_rent_info_invalid_status(self):
        # 提供一个无效的 status 参数
        response = self.client.post(reverse('ManagerGetRentInfo'), {
            'status': 999  # 无效状态
        })

        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        self.assertEqual(response_data['errno'], 0)
        self.assertEqual(len(response_data['data']), 0)  # 无租赁记录符合此状态
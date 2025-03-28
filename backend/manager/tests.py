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
        response = self.client.get(reverse('ManagerGetRentInfo'), {
            'status': 1
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")

    def test_manager_get_rent_info_no_status_param(self):
        response = self.client.post(reverse('ManagerGetRentInfo'))

        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        self.assertEqual(response_data['errno'], 0)
        self.assertEqual(len(response_data['data']), 2)

    def test_manager_get_rent_info_invalid_status(self):
        response = self.client.post(reverse('ManagerGetRentInfo'), {
            'status': 999
        })

        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        self.assertEqual(response_data['errno'], 0)
        self.assertEqual(len(response_data['data']), 0)


class ReviewRentTest(TestCase):
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

    def test_review_rent_success(self):
        response = self.client.post(reverse('reviewRent'), {
            'rentId': self.rent1.rentId,
            'status': 1
        })

        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        self.assertEqual(response_data['errno'], 0)
        self.assertEqual(response_data['msg'], "review success")

        self.rent1.refresh_from_db()
        self.assertEqual(self.rent1.status, 1)

    def test_review_rent_invalid_method(self):
        response = self.client.get(reverse('reviewRent'), {
            'rentId': self.rent1.rentId,
            'status': 1
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")


class GetUserInfoTest(TestCase):
    def setUp(self):
        self.client = self.client_class()

        self.user1 = User.objects.create(
            userId=1,
            userName="danny",
            password="testpassword",
            email="danny@example.com"
        )
        self.user2 = User.objects.create(
            userId=2,
            userName="alice",
            password="testpassword",
            email="alice@example.com"
        )

        self.rent1 = Rent.objects.create(
            rentId=1,
            userId=self.user1.userId,
            roomId=1,
            status=1,
            startTime=timezone.now() - timezone.timedelta(days=10),
            endTime=timezone.now() + timezone.timedelta(days=20),
            applyTime=timezone.now() - timezone.timedelta(days=15)
        )

        self.rent2 = Rent.objects.create(
            rentId=2,
            userId=self.user1.userId,
            roomId=2,
            status=1,
            startTime=timezone.now() - timezone.timedelta(days=5),
            endTime=timezone.now() + timezone.timedelta(days=25),
            applyTime=timezone.now() - timezone.timedelta(days=7)
        )

        self.rent3 = Rent.objects.create(
            rentId=3,
            userId=self.user2.userId,
            roomId=3,
            status=1,
            startTime=timezone.now() - timezone.timedelta(days=3),
            endTime=timezone.now() + timezone.timedelta(days=27),
            applyTime=timezone.now() - timezone.timedelta(days=6)
        )

        Bill.objects.create(
            billId=1,
            rentID=self.rent1.rentId,
            status=0,  # unpaid
            createTime=timezone.now(),
            due=timezone.now() + timezone.timedelta(days=7),
            money=100
        )
        Bill.objects.create(
            billId=2,
            rentID=self.rent1.rentId,
            status=1,  # paid
            createTime=timezone.now(),
            due=timezone.now() + timezone.timedelta(days=7),
            money=50
        )
        Bill.objects.create(
            billId=3,
            rentID=self.rent2.rentId,
            status=0,  # unpaid
            createTime=timezone.now(),
            due=timezone.now() + timezone.timedelta(days=7),
            money=200
        )

    def test_get_user_info_success(self):
        response = self.client.post(reverse('getUserInfo'))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['errno'], 0)
        data = response_data['data']
        self.assertEqual(len(data), 2)

        user1_data = next(user for user in data if user['userId'] == self.user1.userId)
        self.assertEqual(user1_data['userId'], self.user1.userId)
        self.assertEqual(user1_data['userName'], self.user1.userName)
        self.assertEqual(user1_data['email'], self.user1.email)

        user2_data = next(user for user in data if user['userId'] == self.user2.userId)
        self.assertEqual(user2_data['userId'], self.user2.userId)
        self.assertEqual(user2_data['userName'], self.user2.userName)
        self.assertEqual(user2_data['email'], self.user2.email)

    def test_get_user_info_invalid_method(self):
        response = self.client.get(reverse('getUserInfo'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")
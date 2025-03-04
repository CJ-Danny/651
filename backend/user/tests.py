from manager.models import *
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from room.models import *
from .models import *


# Create your tests here.
class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(userName='testuser', email='test@example.com', password='password123', type=0)
        self.manager = Manager.objects.create(name='testmanager', email='manager@example.com', password='password456', type=0, status=0)

    def test_login_user(self):
        response = self.client.post(reverse('login'), {
            'email': 'test@example.com',
            'password': 'password123',
            'type': 0
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)
        self.assertIn('token', response.json())

    def test_login_manager(self):
        response = self.client.post(reverse('login'), {
            'email': 'manager@example.com',
            'password': 'password456',
            'type': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)
        self.assertIn('token', response.json())

    def test_login_wrong_password(self):
        response = self.client.post(reverse('login'), {
            'email': 'test@example.com',
            'password': 'wrongpassword',
            'type': 0
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], 'password wrong!')


class RegisterViewTest(TestCase):
    def setUp(self):
        self.verification_code = RegisterCode.objects.create(email='newuser@example.com', code='ABC123')

    def test_register_success(self):
        response = self.client.post(reverse('register'), {
            'userName': 'newuser',
            'password': 'password123',
            'email': 'newuser@example.com',
            'code': 'ABC123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)
        self.assertTrue(User.objects.filter(email='newuser@example.com').exists())

    def test_register_wrong_code(self):
        response = self.client.post(reverse('register'), {
            'userName': 'newuser',
            'password': 'password123',
            'email': 'newuser@example.com',
            'code': 'WRONGCODE'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], 'code error!')
        self.assertFalse(User.objects.filter(email='newuser@example.com').exists())


class GetRentInfoTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.room = Room.objects.create(
            roomId=1,
            number="101",
            name="Deluxe Room",
            imgUrl="http://example.com/image.jpg",
            floor="1",
            price=5000,
            area="50"
        )

        self.rent = Rent.objects.create(
            rentId=1,
            userId=123,
            roomId=self.room.roomId,
            status=1,
            startTime=timezone.now(),
            endTime=timezone.now() + timezone.timedelta(days=30),
            applyTime=timezone.now()
        )

        Bill.objects.create(
            rentID=self.rent.rentId,
            status=0,
            money=2000,
        )

    def test_get_rent_info_success(self):
        response = self.client.post(reverse('getRentInfo'), {'rentId': self.rent.rentId})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 0)
        self.assertIn('rent', response.json()['data'])
        self.assertIn('bills', response.json()['data'])
        self.assertIn('room', response.json()['data'])
        self.assertEqual(response.json()['data']['rent']['rentId'], self.rent.rentId)

    def test_get_rent_info_wrong_method(self):
        response = self.client.get(reverse('getRentInfo'))  # 使用 GET 请求
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], 'wrong method')
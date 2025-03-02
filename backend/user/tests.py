from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from user.models import *
from manager.models import *


# Create your tests here.
from user.token import GetToken, Check


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
        # 创建一个验证码记录
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
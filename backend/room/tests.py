from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from user.models import *
from service.models import *
from room.models import *


class GetRoomsInfoTest(TestCase):
    def setUp(self):
        self.client = self.client_class()

        self.user = User.objects.create(
            userId=123,
            userName="danny",
            password="test",
            email="test@gmail.com"
        )

        self.room1 = Room.objects.create(
            roomId=1,
            number="101",
            name="Deluxe Room",
            imgUrl="http://example.com/image1.jpg",
            floor="1",
            price=5000,
            area="50"
        )
        self.room2 = Room.objects.create(
            roomId=2,
            number="102",
            name="Standard Room",
            imgUrl="http://example.com/image2.jpg",
            floor="2",
            price=3000,
            area="40"
        )

        self.rent1 = Rent.objects.create(
            rentId=1,
            userId=self.user.userId,
            roomId=self.room1.roomId,
            status=1,
            startTime=timezone.now() - timezone.timedelta(days=10),
            endTime=timezone.now() + timezone.timedelta(days=20),
            applyTime=timezone.now() - timezone.timedelta(days=15)
        )

        self.bill1 = Bill.objects.create(
            rentID=self.rent1.rentId,
            status=0,
            createTime=timezone.now() - timezone.timedelta(days=5),
            due=timezone.now() + timezone.timedelta(days=5),
            money=5000
        )

        self.repairOrder1 = Order.objects.create(
            orderID=1,
            userID=self.user.userId,
            roomID=self.room1.roomId,
            status=0,
            submitTime=timezone.now(),
            assignTime=timezone.now(),
            finishTime=timezone.now(),
            method="Repair"
        )

    def test_get_rooms_info_success(self):
        response = self.client.post(reverse('getRoomsInfo'))

        self.assertEqual(response.status_code, 200)

        rooms_data = response.json()['data']
        self.assertEqual(len(rooms_data), 2)

        room_data = next(room for room in rooms_data if room['roomID'] == self.room1.roomId)
        self.assertEqual(room_data['roomID'], self.room1.roomId)
        self.assertEqual(room_data['roomName'], "Deluxe Room")
        self.assertEqual(room_data['status'], 23)
        self.assertEqual(room_data['userName'], self.user.userName)
        self.assertTrue(room_data['startTime'])
        self.assertTrue(room_data['endTime'])

        room_data2 = next(room for room in rooms_data if room['roomID'] == self.room2.roomId)
        self.assertEqual(room_data2['status'], 0)
        self.assertEqual(room_data2['userName'], '')

    def test_get_rooms_info_wrong_method(self):
        response = self.client.get(reverse('getRoomsInfo'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['errno'], 1000)
        self.assertEqual(response.json()['msg'], "wrong method")

    def test_get_rooms_info_no_rent(self):
        room3 = Room.objects.create(
            roomId=3,
            number="103",
            name="Economy Room",
            imgUrl="http://example.com/image3.jpg",
            floor="3",
            price=2000,
            area="30"
        )

        response = self.client.post(reverse('getRoomsInfo'))
        self.assertEqual(response.status_code, 200)

        rooms_data = response.json()['data']
        room_data3 = next(room for room in rooms_data if room['roomID'] == room3.roomId)
        self.assertEqual(room_data3['status'], 0)
        self.assertEqual(room_data3['userName'], '')
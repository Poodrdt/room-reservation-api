from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.test import APITestCase, APIClient

from .views import *
from .serializers import *

class ReservationTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='test_user', password='test_pwd')

    def test_list_room(self):
        url = reverse('room-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_room(self):
        url = reverse('room-list')
        data = {
            'name': 'test_room'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Room.objects.count(), 1)
        self.assertEqual(Room.objects.get().name, 'test_room')

























    # def test_create_reservation(self):
    #     room_id = self.room.id
    #     payload = {
    #         "title": "test_title",
    #         "start": "2019-11-12T10:00:00Z",
    #         "end": "2019-11-12T11:00:00Z",
    #         "room": room_id
    #     }
    #     request = self.client.post('/reservation', payload, format='json')

    #     request.user = self.user



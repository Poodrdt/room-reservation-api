from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.test import (
    APITestCase,
    APIClient,
    APIRequestFactory,
    force_authenticate,
)

from .views import *
from .serializers import *


class CreateRoomTest(APITestCase):

    def setUp(self):
        self.url = reverse("room-list")
        self.user = User.objects.create_user(
            username="test_user", password="test_pwd")
        self.data = {"name": "test_room"}

    def test_can_not_create_room(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_create_room(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadRoomTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_pwd")
        self.data = {"name": "test_room"}
        # self.room = Room.objects.create(self.data)

    def test_can_read_room_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("room-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_can_read_room_detail(self):
    #     response = self.client.get(reverse('room-detail', args=[self.room.id]))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

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

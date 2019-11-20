from django.urls import reverse
from django.contrib.auth.models import AnonymousUser, User
from rest_framework.test import (
    APITestCase,
    APIClient,
    APIRequestFactory,
    force_authenticate,
)

from meeting_room.views import *
from meeting_room.serializers import *


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
        self.room = Room.objects.create(**self.data)

    def test_can_read_room_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("room-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_room_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('room-detail', args=[self.room.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(APITestCase):

    def setUp(self):
        self.data = {"name": "test_room"}
        self.room = Room.objects.create(**self.data)
        self.url = reverse("room-detail", args=[self.room.id])
        self.user = User.objects.create_user(
            username="test_user", password="test_pwd")
        self.data.update({'name': '"test_room_changed'})

    def test_can_update_room(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.data = {"name": "test_room"}
        self.room = Room.objects.create(**self.data)
        self.url = reverse("room-detail", args=[self.room.id])
        self.user = User.objects.create_user(
            username="test_user", password="test_pwd")

    def test_can_delete_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

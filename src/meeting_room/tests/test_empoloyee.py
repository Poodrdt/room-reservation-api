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


class CreateEmpoloyeeTest(APITestCase):

    def setUp(self):
        self.url = reverse("employee-list")
        self.admin = User.objects.create_superuser(
            username="test_admin", password="test_pwd", email="test@test.test")
        self.data = {"username": "test_user", "password": "test_pwd"}

    def test_can_not_create_user(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_create_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadEmpoloyeeTest(APITestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="test_admin", password="test_pwd", email="test@test.test")
        self.data = {"username": "test_user", "password": "test_pwd"}
        self.user = User.objects.create(**self.data)

    def test_can_read_room_list(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse("employee-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_room_detail(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(
            reverse('employee-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateEmpoloyeeTest(APITestCase):

    def setUp(self):
        self.data = {"username": "test_user", "password": "test_pwd"}
        self.user = User.objects.create(**self.data)
        self.url = reverse("employee-detail", args=[self.user.id])
        self.admin = User.objects.create_superuser(
            username="test_admin", password="test_pwd", email="test@test.test")
        self.data.update({'email': 'changed@changed.changed'})

    def test_can_update_room(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.put(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteEmpoloyeeTest(APITestCase):
    def setUp(self):
        self.data = {"username": "test_user", "password": "test_pwd"}
        self.user = User.objects.create(**self.data)
        self.url = reverse("employee-detail", args=[self.user.id])
        self.admin = User.objects.create_superuser(
            username="test_admin", password="test_pwd", email="test@test.test")

    def test_can_delete_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(
            self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

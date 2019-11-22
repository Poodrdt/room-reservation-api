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


class CreateReservationTest(APITestCase):

    def setUp(self):
        self.url = reverse("reservation-list")
        self.user = User.objects.create_user(
            username="test_user", password="test_pwd")
        self.room = Room.objects.create(**{"name": "test_room"})
        self.data = {
            "title": "test_title",
            "start": "2019-11-12T10:00:00Z",
            "end": "2019-11-12T11:00:00Z",
            "room": self.room.id
        }

    def test_can_not_create_reservation(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_time_overlaps(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, self.data)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_create_reservation(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadReservationTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_pwd")
        self.room = Room.objects.create(**{"name": "test_room"})
        self.data = {
            "title": "test_title",
            "start": "2019-11-12T10:00:00Z",
            "end": "2019-11-12T11:00:00Z",
            "room": self.room,
            "employee_id": self.user.id
        }
        self.reservation = Reservation.objects.create(**self.data)

    def test_can_read_reservation_list(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse("reservation-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_reservation_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            reverse('reservation-detail', args=[self.reservation.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateReservationTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_pwd")
        self.room = Room.objects.create(**{"name": "test_room"})
        self.data = {
            "title": "test_title",
            "start": "2019-11-12T10:00:00Z",
            "end": "2019-11-12T11:00:00Z",
            "room": self.room,
            "employee_id": self.user.id
        }
        self.reservation = Reservation.objects.create(**self.data)
        self.url = reverse("reservation-detail", args=[self.reservation.id])
        self.data.update({
            "title": "test_title_changed",
            "start": "2019-11-12T10:00:00Z",
            "end": "2019-11-12T11:00:00Z",
            "room": self.room.id,
            "employee_id": self.user.id
        })

    def test_can_update_reservation(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url, self.data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="test_pwd")
        self.room = Room.objects.create(**{"name": "test_room"})
        self.data = {
            "title": "test_title",
            "start": "2019-11-12T10:00:00Z",
            "end": "2019-11-12T11:00:00Z",
            "room": self.room,
            "employee_id": self.user.id
        }
        self.reservation = Reservation.objects.create(**self.data)
        self.url = reverse("reservation-detail", args=[self.reservation.id])

    def test_can_delete_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

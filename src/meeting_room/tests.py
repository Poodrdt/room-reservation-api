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


class RoomListTest(APITestCase):
    def setUp(self):
        names = [f"Room{i}" for i in range(5)]
        map(lambda r: Room.objects.create(name=r), names)
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="test_user", password="test_pwd")
        self.view = RoomViewset.as_view({"get": "list"})

    def test_get_all_rooms_authorized(self):
        url = reverse("room-list")
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        # request.user = self.user
        # response = self.client.get(url)
        # rooms = Room.objects.all()
        response = self.view(request)
        # serializer = RoomSerializer(rooms, many=True)
        # self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_all_rooms_unauthorized(self):
    #     url = reverse("room-list")
    #     response = self.client.get(url)
    #     rooms = Room.objects.all()
    #     serializer = RoomSerializer(rooms, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_room(self):
    #     url = reverse("room-list")
    #     data = {"name": "test_room"}
    #     response = self.client.post(url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Room.objects.count(), 1)
    #     self.assertEqual(Room.objects.get().name, "test_room")
    #     self.assertEqual(response.data.get("name"), "test_room")

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


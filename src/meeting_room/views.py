from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import viewsets, generics, status, permissions
from django.contrib.auth import get_user_model
from .models import Reservation, Room
from .serializers import (
    RoomSerializer,
    ReservationSerializer,
    ReservationCreateSerializer,
    UserSerializer,
)

User = get_user_model()


class UserViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoomViewset(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReservationSerializer
    filterset_fields = ('employee', 'room')

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'create':
            serializer_class = ReservationCreateSerializer

        if self.action == 'update' or self.action == 'partial_update':
            serializer_class = ReservationCreateSerializer

        return serializer_class

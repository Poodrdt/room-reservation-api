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
import datetime
from django.utils.timezone import utc

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
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ReservationSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'create':
            serializer_class = ReservationCreateSerializer

        if self.action == 'update' or self.action == 'partial_update':
            serializer_class = ReservationCreateSerializer

        return serializer_class

    def get_queryset(self, **kwargs):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        # queryset = Reservation.objects.filter(start__gt=now)
        queryset = Reservation.objects.all()
        user_filter = self.request.query_params.get("user_filter", None)
        if user_filter is not None:
            queryset = queryset.filter(employee__id=user_filter)
        return queryset

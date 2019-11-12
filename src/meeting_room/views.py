from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from django.contrib.auth import get_user_model
from .models import Reservation, Room
from .serializers import (
    RoomSerializer,
    ReservationSerializer,
    UserSerializer,
)
import datetime
from django.utils.timezone import utc

User = get_user_model()


class UserViewset(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomViewset(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationViewset(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self, **kwargs):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        # queryset = Reservation.objects.filter(start__gt=now)
        queryset = Reservation.objects.all()
        user_filter = self.request.query_params.get("user_filter", None)
        if user_filter is not None:
            queryset = queryset.filter(employee__username=user_filter)
        return queryset
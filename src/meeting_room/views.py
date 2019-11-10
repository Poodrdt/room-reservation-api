from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from .models import Reservation
from .serializers import (
    EmployeeSerializer,
    RoomSerializer,
    ReservationSerializer,
    UserSerializer,
)
import datetime
from django.utils.timezone import utc


class UserList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewset(viewsets.ViewSet):
    serializer_class = EmployeeSerializer


class RoomViewset(viewsets.ViewSet):
    serializer_class = RoomSerializer


class ReservationViewset(viewsets.ViewSet):
    serializer_class = ReservationSerializer

    # def post(self, request):

    def get_queryset(self, **kwargs):
        now = datetime.datetime.utcnow().replace(tzinfo=utc)
        queryset = Reservation.objects.filter(from_time_gt=now)
        user_filter = self.request.query_params.get("user_filter", None)
        if username is not None:
            queryset = queryset.filter(employee__user__username=user_filter)
        return queryset

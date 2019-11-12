from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Room, Reservation

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = []
        fields = ('id', 'password', 'username', 'first_name', 'last_name')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        exclude = ()

    def validate(self, data):
        start, end, room = data['start'], data['end'], data['room']
        if start > end:
            raise serializers.ValidationError("End must occur after start")
        overlap = Reservation.objects.filter(   
            Q(start__lte=start, end__gt=start) |
            Q(start__lt=end, end__gte=end) |
            Q(start__gt=start, end__lt=end)
            )
        if overlap.exists():
            raise serializers.ValidationError(f"Room is already reserved {overlap[0]}")
        return data


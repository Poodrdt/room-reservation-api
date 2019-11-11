from rest_framework import serializers
from django.contrib.auth import get_user_model
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
        exclude = []


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        exclude = []

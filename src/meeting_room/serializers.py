from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee, Room, Reservation

User = get_user_model()


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = []


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = []
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'email', 'employee')

    def create(self, validated_data):
        user = super().create(validated_data)
        employee = Employee.objects.create(
            user=user
        )
        return user


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = []


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        exclude = []

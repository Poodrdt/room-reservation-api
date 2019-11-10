from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee, Room, Reservation

User = get_user_model()


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(required=True)

    class Meta:
        model = User
        fields = (
            "url",
            "email",
            "employee",
            "created",
        )

    def create(self, validated_data):

        # create user
        user = User.objects.create(
            url=validated_data["url"],
            email=validated_data["email"],
            # etc ...
        )

        # employee_data = validated_data.pop("employee")
        # create employee
        employee = Employee.objects.create(
            user=user
            # first_name = employee_data['first_name'],
            # last_name = employee_data['last_name'],
            # # etc...
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

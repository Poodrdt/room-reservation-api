from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Room, Reservation

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "password", "username", "first_name", "last_name")

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()


class ReservationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "title", "start", "end",
                  "room", "employee")


class ReservationPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id", "title", "start", "end",
                  "room", "employee", "reserved_by")


class ReservationSerializer(serializers.ModelSerializer):

    employee = serializers.HiddenField(
        default=serializers.CurrentUserDefault())

    reserved_by = serializers.CharField(source="employee", read_only=True)

    class Meta:
        model = Reservation
        fields = ("id", "title", "start", "end",
                  "room", "employee", "reserved_by")

    def validate(self, data):
        start, end, room = data["start"], data["end"], data["room"]
        if start > end:
            raise serializers.ValidationError("End must occur after start")
        overlap = Reservation.objects.filter(
            Q(start__lte=start, end__gt=start)
            | Q(start__lt=end, end__gte=end)
            | Q(start__gt=start, end__lt=end),
            room=room,
        )
        if overlap.exists():
            raise serializers.ValidationError(
                f"This room is already reserved at {overlap[0]}"
            )
        return data

    def validate_employee(self, value):
        if value.is_anonymous:
            raise serializers.ValidationError(
                f"Can not reserve under Anonymous user")
        return value

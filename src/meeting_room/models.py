from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Room(models.Model):
    name = models.CharField(max_length=255)

    def is_vacant(self, start, end):
        if time in self.reservation_set():
            return False
        return True


class Reservation(models.Model):
    title = models.CharField(max_length=255)
    emploee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

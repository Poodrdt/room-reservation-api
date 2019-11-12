from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Reservation(models.Model):
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return str(self.title) + str(self.start) + str(self.end)
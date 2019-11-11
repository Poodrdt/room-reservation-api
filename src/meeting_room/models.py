from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class Room(models.Model):
    name = models.CharField(max_length=255)

    def is_vacant(self, start, end):
        overlap = Reservation.objects.filter(Q(pk=self.pk) & (Q(start__lte=start) | Q(end__gte=end))).exists()
        if overlap:
            return False
        return True


class Reservation(models.Model):
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

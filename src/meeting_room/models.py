from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Employee(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Room():
    name = models.CharField(max_length=255)
    def is_occupied(self, time):
        return True

class Reservation():
    title = models.CharField(max_length=255)
    emploee = models.ForeignKey(Employee)
    room = models.ForeignKey(Room)
    start = models.DateTimeField()
    end = models.DateTimeField()
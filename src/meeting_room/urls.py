from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewset, RoomViewset, ReservationViewset

router = routers.DefaultRouter()
router.register(r"employee", EmployeeViewset, base_name="employee")
router.register(r"room", RoomViewset, base_name="room")
router.register(r"reservation", ReservationViewset, base_name="reservation")

urlpatterns = router.urls


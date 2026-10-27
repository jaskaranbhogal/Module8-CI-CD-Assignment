from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, api_status

router = DefaultRouter()
router.register("rooms", RoomViewSet, basename="room")

urlpatterns = [
    path("status/", api_status, name="api-status"),
    *router.urls,
]

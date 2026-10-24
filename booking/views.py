from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Room
from .serializers import RoomSerializer


class RoomViewSet(ReadOnlyModelViewSet):
    queryset = Room.objects.all().order_by("id")
    serializer_class = RoomSerializer

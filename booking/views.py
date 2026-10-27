from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Room
from .serializers import RoomSerializer


@api_view(["GET"])
def api_status(request):
    return Response({"service": "study-room-booking", "status": "ok"})


class RoomViewSet(ReadOnlyModelViewSet):
    queryset = Room.objects.all().order_by("id")
    serializer_class = RoomSerializer

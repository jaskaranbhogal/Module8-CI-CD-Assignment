from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Room


class RoomAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.room = Room.objects.create(
            name="Library Study Room A",
            building="Campus Library",
            capacity=4,
            is_available=True,
        )

    def test_list_rooms_returns_200_and_room_data(self):
        response = self.client.get(reverse("room-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Library Study Room A")
        self.assertEqual(response.data[0]["capacity"], 4)

    def test_room_detail_returns_availability(self):
        response = self.client.get(reverse("room-detail", args=[self.room.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["is_available"])
        self.assertEqual(response.data["building"], "Campus Library")

    def test_unknown_room_returns_404(self):
        response = self.client.get(reverse("room-detail", args=[9999]))
        self.assertEqual(response.status_code, 404)

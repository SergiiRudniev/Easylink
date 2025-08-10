from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class TicketAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="u", password="p")
        self.client.force_authenticate(self.user)

    def test_create_and_list_ticket(self):
        response = self.client.post(
            "/api/support/tickets/",
            {"subject": "Help", "message": "Need assistance"},
        )
        self.assertEqual(response.status_code, 201)

        list_response = self.client.get("/api/support/tickets/")
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.data), 1)
        self.assertEqual(list_response.data[0]["subject"], "Help")
        self.assertEqual(list_response.data[0]["status"], "open")

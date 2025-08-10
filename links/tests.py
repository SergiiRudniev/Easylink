from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class ShortLinkAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="u", password="p")
        self.client.force_authenticate(self.user)

    def test_create_and_follow_link(self):
        response = self.client.post("/api/links/", {"original_url": "https://example.com"})
        self.assertEqual(response.status_code, 201)
        slug = response.data["slug"]
        follow_response = self.client.get(f"/api/{slug}/")
        self.assertEqual(follow_response.status_code, 302)

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

class APIKeyAuthTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="u", password="p")
        self.client.force_authenticate(self.user)

    def test_create_and_use_api_key(self):
        create = self.client.post("/api/keys/", {})
        self.assertEqual(create.status_code, 201)
        key = create.data["key"]
        self.client.force_authenticate(user=None)
        response = self.client.post(
            "/api/links/",
            {"original_url": "https://example.com"},
            HTTP_X_API_KEY=key,
        )
        self.assertEqual(response.status_code, 201)

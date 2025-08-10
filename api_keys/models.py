from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()

def generate_key():
    return get_random_string(40)

class APIKey(models.Model):
    user = models.ForeignKey(User, related_name="api_keys", on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True, default=generate_key)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.key}"

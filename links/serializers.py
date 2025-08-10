from rest_framework import serializers
from .models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortLink
        fields = ["id", "slug", "original_url", "group", "domain", "pixel", "created_at"]
        read_only_fields = ["slug", "created_at"]

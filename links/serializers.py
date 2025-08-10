from rest_framework import serializers
from .models import ShortLink, LinkGroup, Domain, Pixel


class LinkGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkGroup
        fields = ["id", "name"]


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["id", "name", "verified"]
        read_only_fields = ["verified"]


class PixelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pixel
        fields = ["id", "service", "code"]


class ShortLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortLink
        fields = ["id", "slug", "original_url", "group", "domain", "pixel", "created_at"]
        read_only_fields = ["slug", "created_at"]

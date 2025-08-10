from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "id",
            "subject",
            "message",
            "response",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["response", "status", "created_at", "updated_at"]

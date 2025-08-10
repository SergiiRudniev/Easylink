from django.shortcuts import get_object_or_404, redirect
from django.http import HttpRequest
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ShortLink, Click
from .serializers import ShortLinkSerializer


class ShortLinkViewSet(viewsets.ModelViewSet):
    serializer_class = ShortLinkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ShortLink.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(["GET"])
def follow_link(request: HttpRequest, slug: str):
    link = get_object_or_404(ShortLink, slug=slug)
    Click.objects.create(
        link=link,
        user_agent=request.META.get("HTTP_USER_AGENT", ""),
        referer=request.META.get("HTTP_REFERER", ""),
        ip_address=request.META.get("REMOTE_ADDR", "0.0.0.0"),
    )
    return redirect(link.original_url)

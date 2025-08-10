from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ShortLinkViewSet,
    LinkGroupViewSet,
    DomainViewSet,
    PixelViewSet,
    follow_link,
)

router = DefaultRouter()
router.register("links", ShortLinkViewSet, basename="link")
router.register("groups", LinkGroupViewSet, basename="group")
router.register("domains", DomainViewSet, basename="domain")
router.register("pixels", PixelViewSet, basename="pixel")

urlpatterns = [
    path("", include(router.urls)),
    path("<slug:slug>/", follow_link, name="follow-link"),
]

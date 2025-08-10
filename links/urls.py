from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ShortLinkViewSet, follow_link

router = DefaultRouter()
router.register("links", ShortLinkViewSet, basename="link")

urlpatterns = [
    path("", include(router.urls)),
    path("<slug:slug>/", follow_link, name="follow-link"),
]

from rest_framework.routers import DefaultRouter
from .views import APIKeyViewSet

router = DefaultRouter()
router.register("keys", APIKeyViewSet, basename="apikey")

urlpatterns = router.urls

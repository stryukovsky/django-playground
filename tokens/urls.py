from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TokenViewSet, AssetViewSet

router = DefaultRouter()
router.register("tokens", TokenViewSet)
router.register("assets", AssetViewSet)

urlpatterns = router.urls

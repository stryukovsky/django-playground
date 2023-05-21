from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TokenViewSet

router = DefaultRouter()
router.register("tokens", TokenViewSet)

urlpatterns = router.urls

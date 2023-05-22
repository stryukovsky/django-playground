from django.urls import path
from rest_framework.routers import DefaultRouter 

from .views import TokenViewSet, AssetViewSet, BalanceOfView, TransferFromView

router = DefaultRouter()
router.register("tokens", TokenViewSet)
router.register("assets", AssetViewSet)

urlpatterns = router.urls
urlpatterns += [path("balance_of", BalanceOfView.as_view())]
urlpatterns += [path("transfer_from", TransferFromView.as_view())]

from rest_framework.viewsets import ModelViewSet
from .serializers import TokenSerializer, AssetSerializer
from .models import Token, Asset

class TokenViewSet(ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

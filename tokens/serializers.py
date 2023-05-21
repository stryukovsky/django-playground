from rest_framework.serializers import ModelSerializer

from .models import Token, Asset


class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"

class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"

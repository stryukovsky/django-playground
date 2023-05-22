from rest_framework.serializers import ModelSerializer, Serializer, CharField, DecimalField

from .models import Token, Asset


class TokenSerializer(ModelSerializer):
    class Meta:
        model = Token
        fields = "__all__"


class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"


class TransferFromSerializer(Serializer):
    asset = CharField(max_length=42)
    sender = CharField(max_length=42)
    recipient = CharField(max_length=42)
    amount = DecimalField(max_digits=78, decimal_places=0)

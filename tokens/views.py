from rest_framework.viewsets import ModelViewSet
from .serializers import TokenSerializer, AssetSerializer, TransferFromSerializer
from .models import Token, Asset
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


class TokenFilterSet(filters.FilterSet):
    holder = filters.CharFilter(field_name="holder", lookup_expr="iexact")


class TokenViewSet(ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    filterset_fields = ("holder", )


class AssetFilterSet(filters.FilterSet):
    holder = filters.CharFilter(field_name="holder", lookup_expr="iexact")


class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filterset_fields = ("holder", )


class BalanceOfView(APIView):

    def get(self, request: Request, format=None) -> Response:
        if not (holder := request.query_params.get("holder")):
            return Response({"error": "no holder provided"}, status=HTTP_400_BAD_REQUEST)

        balance = {
            "tokens": TokenSerializer(instance=Token.objects.filter(holder__iexact=holder), many=True).data,
            "assets": AssetSerializer(instance=Asset.objects.filter(holder__iexact=holder), many=True).data,
        }
        return Response(balance, status=HTTP_200_OK)


class TransferFromView(APIView):

    def post(self, request: Request, format=None) -> Response:
        transfer_from = TransferFromSerializer(data=request.data)
        transfer_from.is_valid()
        asset: str = transfer_from.data.get("asset")
        sender: str = transfer_from.data.get("sender")
        recipient: str = transfer_from.data.get("recipient")
        amount: int = int(transfer_from.data.get("amount"))
        if not (sender_balance := Asset.objects.filter(address=asset, holder=sender).first()):
            return Response({"error": "asset or sender's balance does not exist"})
        if sender_balance.balance < amount:
            return Response({"error": "transfer amount is greater than sender balance"})
        if not (recipient_balance := Asset.objects.filter(address=asset, holder=recipient).first()):
            recipient_balance = Asset.objects.create(
                address=asset, holder=recipient, balance=amount)
        else:
            recipient_balance.balance += amount
        sender_balance.balance -= amount
        sender_balance.save()
        recipient_balance.save()
        return Response({"transfer": "success", "sender": sender, "recipient": recipient, "amount": amount, "asset": asset})

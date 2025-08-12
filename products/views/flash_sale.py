from rest_framework import viewsets
from ..models import FlashSale
from ..serializers import FlashSaleSerializer
from rest_framework.permissions import IsAuthenticated


class FlashSaleViewSet(viewsets.ModelViewSet):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleSerializer
    permission_classes = [IsAuthenticated]
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from ..models import FlashSale
from ..permissions import IsAdminOrReadOnly
from ..serializers import FlashSaleSerializer
from rest_framework.permissions import IsAuthenticated
from ..filters import FlashSaleFilter
from rest_framework import filters


class FlashSaleViewSet(viewsets.ModelViewSet):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = FlashSaleFilter

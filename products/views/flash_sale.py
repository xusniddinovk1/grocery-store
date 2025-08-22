from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from ..models import FlashSale
from ..permissions import IsAdminOrReadOnly
from ..serializers import FlashSaleSerializer
from rest_framework.permissions import IsAuthenticated
from ..filters import FlashSaleFilter
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class FlashSaleViewSet(viewsets.ModelViewSet):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = FlashSaleFilter

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('min_discount_percentage', openapi.IN_QUERY, description='Minimum narxi',
                          type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_discount_percentage', openapi.IN_QUERY, description='Maksimum narxi',
                          type=openapi.TYPE_NUMBER),
        openapi.Parameter('product', openapi.IN_QUERY, description='Mahsulot nomi',
                          type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

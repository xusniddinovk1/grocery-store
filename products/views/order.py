from rest_framework import viewsets
from ..models import Order
from ..serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsAdminOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

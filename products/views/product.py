from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers import CategorySerializer, ProductSerializer
from ..models import Category, Product
from ..permissions import IsAdminOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

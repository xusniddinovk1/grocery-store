from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..filters import ProductFilter, CategoryFilter
from ..serializers import CategorySerializer, ProductSerializer
from ..models import Category, Product
from ..permissions import IsAdminOrReadOnly
from django_filters import rest_framework as django_filters
from rest_framework import filters


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CategoryFilter

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description='Kategoriya nomi',
                          type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('min_price', openapi.IN_QUERY, description="Narxdan katta yoki teng",
                          type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_price', openapi.IN_QUERY, description="Narxdan kichik yoki teng",
                          type=openapi.TYPE_NUMBER),
    ])
    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category', None)
        if category:
            self.queryset = self.queryset.filter(category=category)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        related_products = Product.objects.filter(category=instance.category).exclude(id=instance.id)[:5]
        related_serializer = ProductSerializer(related_products, many=True)
        return Response({
            'product': serializer.data,
            'related_product': related_serializer.data
        })

    @action(detail=True, methods=['get'])
    def avg_rating(self, request, pk=None):
        product = self.get_object()
        comments = product.comments.all()

        if comments.count() == 0:
            return Response({'average_rating': 'No comments yet'})

        avg_rating = sum([comment.rating for comment in comments]) / comments.count()
        return Response({'average_rating': round(avg_rating, 2)})

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from ..filters import CommentFilter
from ..permissions import IsOwnerOrReadOnly
from ..serializers import CommentSerializer
from ..models import Comment, OrderItem
from django_filters import rest_framework as django_filters
from rest_framework import filters


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CommentFilter

    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.validated_data['product']

        if not OrderItem.objects.filter(order__user=user, product=product).exists():
            raise ValidationError("Siz bu kitobni sotib olmagansiz, izoh qoldirolmaysiz.")

        serializer.save(user=user)

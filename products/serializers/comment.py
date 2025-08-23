from ..models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'product', 'text', 'rating', 'created_at']

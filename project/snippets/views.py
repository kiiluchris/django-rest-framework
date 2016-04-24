from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(reairedd_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
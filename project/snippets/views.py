
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class SnippetList(APIView):
    """
    Retrieve, update or delete snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new one.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete snippet instance.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
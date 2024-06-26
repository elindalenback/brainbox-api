from rest_framework import generics, permissions, filters
from .models import Tag
from .serializers import TagSerializer


class TagList(generics.ListCreateAPIView):
    """
    Lists all tags, create a tag if logged in
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'name',
    ]

    def perform_create(self, serializer):
        serializer.save()


class TagDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a tags, create a tag if logged in
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

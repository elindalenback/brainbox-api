from django.db.models import Count
from rest_framework import generics, permissions, filters
from brainbox_api.permissions import IsOwnerOrReadOnly
from .models import Note
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    """
    List notes or create a note if logged in
    The perform_create method associates the note with the logged in user.
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Note.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a note and edit or delete it if you own it.
    """
    serializer_class = NoteSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Note.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
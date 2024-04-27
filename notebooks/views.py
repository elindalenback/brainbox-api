from rest_framework import generics, permissions
from brainbox_api.permissions import IsOwnerOrReadOnly
from .models import Notebook
from .serializers import NotebookSerializer


class NotebookList(generics.ListCreateAPIView):
    """
    List all notebooks or create a notebook if logged in.
    The perform_create method associates the notebook with the logged in user.
    """
    serializer_class = NotebookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Notebook.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotebookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a notebook and edit or delete it if you own it.
    """
    serializer_class = NotebookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Notebook.objects.all()

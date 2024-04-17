from django.http import Http404
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.apps import apps
from brainbox_api.permissions import IsOwnerOrReadOnly

from .models import Note
from .serializers import NoteSerializer


class NoteList(APIView):
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(
            notes, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = NoteSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class NoteDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = NoteSerializer

    def get_object(self, pk):
        try:
            note = Note.objects.get(pk=pk)
            self.check_object_permissions(self.request, note)
            return note
        except Note.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(
            note, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(
            note, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        note = self.get_object(pk)
        note.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
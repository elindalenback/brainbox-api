from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.apps import apps

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
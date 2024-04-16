from rest_framework import serializers
from .models import Notebook
from notes.serializers import NoteSerializer

class NotebookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    notes = NoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = Notebook
        fields = ['id', 'owner', 'name', 'folder_image', 'notes']

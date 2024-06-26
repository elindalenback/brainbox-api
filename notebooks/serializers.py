from rest_framework import serializers
from .models import Notebook
from notes.serializers import NoteSerializer


class NotebookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    notes = serializers.StringRelatedField(many=True, read_only=True)
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_folder_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    class Meta:
        model = Notebook
        fields = ['id', 'owner', 'name', 'folder_image', 'notes', 'is_owner']

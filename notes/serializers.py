from rest_framework import serializers
from .models import Note
from tags.models import Tag
from notebooks.models import Notebook
from tags.serializers import TagSerializer
from likes.models import Like

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    
    notebook = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Notebook.objects.all(),
        allow_null=True,
        required=False
    )
    tags_data = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, note=obj
            ).first()
            return like.id if like else None
        return None

    def get_tags_data(self, obj):
        if obj.tags:
            tags = Tag.objects.filter(
                id__in=obj.tags.values_list('id', flat=True)
            )
            return TagSerializer(tags, many=True).data
        return []

    class Meta:
        model = Note
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'notebook', 'deleted',
            'like_id', 'likes_count', 'comments_count', 'tags_data',
        ]
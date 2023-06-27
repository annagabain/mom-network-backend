from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='created_by.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='created_by.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.created_by

    class Meta:
        model = Post
        fields = ['id', 'created_by', 'content', 'created_at',
                  'updated_at', 'post_image', 'profile_id',
                  'profile_image', 'is_owner']

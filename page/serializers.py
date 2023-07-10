from rest_framework import serializers
from django.contrib.auth.models import User
from posts.serializers import PostSerializer
from .models import Page


class PageSerializer(serializers.ModelSerializer):
    admin_username = serializers.ReadOnlyField(source='admin.username')
    followers_count = serializers.SerializerMethodField()
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ['id', 'admin', 'admin_username', 'title', 'icon', 'description', 'image', 'followers', 'followers_count', 'posts']
        extra_kwargs = {
            'followers': {'required': False},
        }

    def get_followers_count(self, obj):
        return obj.followers.count()

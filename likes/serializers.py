from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    postContent = serializers.ReadOnlyField(source='post.content')

    class Meta:
        model = Like
        fields = ['id', 'owner', 'post', 'postContent']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate, you have already liked this post!'
            })

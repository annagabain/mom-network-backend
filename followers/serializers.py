from rest_framework import serializers
from .models import Follower
from django.db import IntegrityError


class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    person_followed_name = serializers.ReadOnlyField(
        source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'created_at',
                  'followed', 'person_followed_name']
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate, you have already followed this person!'
            })

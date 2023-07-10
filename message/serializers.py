from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'sender_username', 'recipient', 'recipient_username', 
                'title', 'message_content', 'created_at']

    def validate_sender(self, value):
        current_user = self.context.get('current_user')
        if value != current_user:
            raise serializers.ValidationError(
                "Make sure you are the sender of this message.")
        return value

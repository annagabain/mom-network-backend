from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'title', 'message_content', 
                  'sender_username',  'recipient_username', 'created_at']

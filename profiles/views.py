from api_for_mom.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer
from django.db.models import Count
# from rest_framework import generics, filters
from rest_framework import generics, permissions, filters



class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True)
    ).order_by('-created_at')
    
    serializer_class = ProfileSerializer
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticated]  # Logged in users can see the list of all profiles
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count = Count('owner__post', distinct=True),
        followers_count = Count('owner__followed', distinct=True),
        following_count = Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer

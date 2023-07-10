from .models import Post
from .serializers import PostSerializer
from api_for_mom.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from rest_framework import generics, permissions, filters


class PostList(generics.ListCreateAPIView):
    # serializer_class creates a form with the serializer fields
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comments', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # serializer_class creates a form with the serializer fields
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comments', distinct=True)
    ).order_by('-created_at')

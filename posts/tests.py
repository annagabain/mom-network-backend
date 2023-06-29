from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient
from .models import Post
from .serializers import PostSerializer
from .views import PostList, PostDetail


class PostListTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='testuser')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.post_data = {
            'created_by': self.user.id,
            'content': 'Test content',
            'post_image': 'path/to/image.jpg'
        }

    def test_post_list_get(self):
        Post.objects.create(created_by=self.user, content='Test content 1')
        Post.objects.create(created_by=self.user, content='Test content 2')

        request = self.factory.get('/posts/')
        response = PostList.as_view()(request)

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_post_list_post(self):
        request = self.factory.post('/posts/', data=self.post_data, format='json')
        response = PostList.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().created_by, self.user)

class PostDetailTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='testuser')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(created_by=self.user, content='Test content')

    def test_post_detail_get(self):
        request = self.factory.get('/posts/1/')
        response = PostDetail.as_view()(request, pk=self.post.id)

        serializer = PostSerializer(self.post, context={'request': request})
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_post_detail_put(self):
        updated_content = 'Updated content'
        updated_data = {
            'created_by': self.user.id,
            'content': updated_content,
            'post_image': 'path/to/updated_image.jpg'
        }

        request = self.factory.put('/posts/1/', data=updated_data, format='json')
        response = PostDetail.as_view()(request, pk=self.post.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().content, updated_content)

    def test_post_detail_delete(self):
        request = self.factory.delete('/posts/1/')
        response = PostDetail.as_view()(request, pk=self.post.id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

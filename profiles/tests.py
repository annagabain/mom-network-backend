from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer


class ProfileListTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.owner = User.objects.create(username='NewUserTest')
        Profile.objects.create(owner=self.owner, bio='Bio 1')
        Profile.objects.create(owner=self.owner, bio='Bio 2')
        self.client = APIClient()

    def test_get_profile_list(self):
        url = '/profiles/'
        response = self.client.get(url)
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


# class ProfileDetailTestCase(TestCase):
#     def setUp(self):
#         # Create test data
#         self.owner = User.objects.create(username='NewUserTest')
#         self.profile = Profile.objects.create(owner=self.owner, bio='Test Bio')
#         self.client = APIClient()

#     def test_get_profile_detail(self):
#         url = f'/profiles/{self.profile.pk}/'
#         response = self.client.get(url)
#         serializer = ProfileSerializer(self.profile)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)

#     def test_update_profile_detail(self):
#         url = f'/profiles/{self.profile.pk}/'
#         data = {
#             'owner': self.owner.username,
#             'bio': 'Updated Bio'
#         }
#         response = self.client.put(url, data)
#         self.profile.refresh_from_db()
#         serializer = ProfileSerializer(self.profile)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(self.profile.bio, 'Updated Bio')

#     def test_delete_profile(self):
#         url = f'/profiles/{self.profile.pk}/'
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Profile.objects.filter(pk=self.profile.pk).exists())

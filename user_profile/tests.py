from django.test import TestCase
from rest_framework.test import APIClient

class ProfileUpdateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test profile
        self.profile = Profile.objects.create(user="Test Name", bio="")
    
    def test_profile_update(self):
        url = f"/profiles/{self.profile.pk}/"
        data = {
            "user": "Anna",
            "bio": "hello"
        }
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, 200)
        # Verify the updated fields in the response
        self.assertEqual(response.data['user'], "Anna")
        self.assertEqual(response.data['bio'], "hello")

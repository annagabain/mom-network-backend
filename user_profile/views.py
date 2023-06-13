from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(APIView):
    def get(self, request):
        user_profile = Profile.objects.all()
        serializer = ProfileSerializer(user_profile, many=True)
        return Response(serializer.data)
    # return Response(user_profile)

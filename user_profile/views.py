from django.http import Http404
from rest_framework import status
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


class ProfileDetail(APIView):
    def get_object(self, pk):
        try:
            specific_profile = Profile.objects.get(pk=pk)
            return specific_profile
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        specific_profile = self.get_object(pk)
        serializer = ProfileSerializer(specific_profile)
        return Response(serializer.data)
    
    def put(self, request, pk):
        specific_profile = self.get_object(pk)
        serializer = ProfileSerializer(specific_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        specific_profile = self.get_object(pk)
        specific_profile.delete()
        return Response(status=204)

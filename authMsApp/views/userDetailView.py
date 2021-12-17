from authMsApp.models.user import User
from authMsApp.serializers.userSerializer import UserSerializer
from django.conf import settings
from rest_framework import generics, status
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
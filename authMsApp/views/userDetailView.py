from authMsApp.models.user import User
from authMsApp.serializers.userSerializer import UserSerializer
from rest_framework import generics


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

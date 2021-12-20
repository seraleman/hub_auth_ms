from rest_framework import serializers
from authMsApp.models.user import User
from authMsApp.models.role import Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

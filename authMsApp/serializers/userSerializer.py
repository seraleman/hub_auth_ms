from rest_framework import serializers
from authMsApp.models.user import User
from authMsApp.models.role import Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "date_of_birth",
            "document",
            "document_type",
            "email",
            "enabled",
            "entity",
            "full_name",
            "password",
            "phoneNumber",
            "position",
            "role",
        ]

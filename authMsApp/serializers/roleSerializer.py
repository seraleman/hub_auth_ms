from rest_framework import serializers
from authMsApp.models.role import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

from authMsApp.serializers.userSerializer import UserSerializer
from rest_framework import views, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response


class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "email": request.data["email"],
            "password": request.data["password"],
        }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

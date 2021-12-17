from authMsApp import views
from authMsApp.models.user import User
from authMsApp.serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework import views

class UserView(views.APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        seriliazer = UserSerializer(users, many= True)
        return Response(seriliazer.data)

    def put(self, request, pk, format=None):
        
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
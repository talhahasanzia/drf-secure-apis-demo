# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView

from oauth_django.messages import *
from .serializers import *


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):

        user = UserRequestSerializer(data=request.data)

        if user.is_valid():
            username = user.data.get('username')
            email = user.data.get('email')
            password = user.data.get('password')
            User.objects.create_user(username, email, password)
            # token, _ = Token.objects.get_or_create(user=user)
            # print(token)
            return success(200)
        else:
            print(user.errors)
            return failure(400, message_from_errors(user.errors))


class UserView(APIView):

    def get(self, request):
        current_user = User.objects.get(username=self.request.user)
        serialized = UserResponseSerializer(current_user)
        return success(200, serialized.data)

    # def delete(self, request):
    #     username = request.data['username']
    #     try:
    #         user = User.objects.get(username=username)
    #         user.delete()
    #     except Exception as e:
    #         return failure(403, str(e))
    #     else:
    #         return empty_success(200)
    #
    # def put(self, request):
    #     user = UserRequestSerializer(data=request.data)
    #
    #     try:
    #         if user.is_valid(raise_exception=True):
    #             user.update(user, user.validated_data)
    #     except Exception as e:
    #         return failure(403, str(e))
    #     else:
    #         return empty_success(200)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAuthSerializer

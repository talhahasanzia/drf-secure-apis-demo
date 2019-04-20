from django.contrib.auth.models import User
from rest_framework import serializers


# first we define the serializers
class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password",)


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email",)


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("username",)

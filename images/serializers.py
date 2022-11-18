from rest_framework import serializers
from dataclasses import field, fields
from images.models import Image, User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'name', 'image', 'user_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nomeCompleto', 'username', 'email', 'password']
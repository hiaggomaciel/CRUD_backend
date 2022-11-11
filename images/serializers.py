from rest_framework import serializers
from images.models import ImageUpload, User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ImageSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    class Meta:
        model = ImageUpload
        fields = ['id', 'name', 'image', 'user', 'creator', 'creator_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nomeCompleto', 'username', 'email', 'password']
from rest_framework import serializers
from images.models import ImageUpload
from django.contrib.auth.models import User

class ImageSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    class Meta:
        model = ImageUpload
        fields = ['id', 'name', 'image', 'user', 'creator', 'creator_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
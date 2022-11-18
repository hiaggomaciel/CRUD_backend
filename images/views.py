from images.serializers import UserSerializer, ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets, generics
from django.shortcuts import render, redirect
from rest_framework.response import Response
from images.models import Image, User
from django.http import FileResponse
from rest_framework import status
from django.contrib.auth import login
from django.contrib import messages
import json


### Lista todos os Usuários ###

class UserViewSet(viewsets.ModelViewSet):
    """Listando todos os usuários"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


### Lista todas as imagens ###

class ImagesViewSet(viewsets.ModelViewSet):
    """Listando todas as imagens do sistema"""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

### Lista todas as imagens de um usuário ###


class ImageListUserViewSet(generics.ListAPIView):
    """Listando todas as imagens de um usuário"""
    def get_queryset(self):
        queryset = Image.objects.filter(user_id=self.kwargs['user_id'])
        return queryset
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

### Lista os dados da imagem ###


class ImageListUserImagesViewSet(generics.ListAPIView):
    """Listando uma imagem de um usuário"""
    def get(self, request, *args, **kwargs):
        queryset = Image.objects.filter(id=self.kwargs['image_id'])
        serializer = ImageSerializer(queryset[0])
        return Response(serializer.data, status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        queryset = Image.objects.filter(
            id=self.kwargs['image_id']).first()
        queryset.delete()
        return Response(status.HTTP_200_OK)

### Retorna o arquivo de imagem ###


def ImageDetailUser(request, user_id, image_id):
    image = Image.objects.get(id=image_id)
    img = open(image.image.path, 'rb')
    return FileResponse(img)

### Upload da imagem ###


class ImagesUpload(generics.CreateAPIView):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.data['data'])
        image = request.FILES.get('image')
        user = User.objects.get(id=data['user'])

        user_image = Image(
            name=data['name'],
            user_id=user,
            image=image)

        user_image.save()
        return Response(status.HTTP_201_CREATED)


### Cadastrando um novo Usuário ###

class Cadastro(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        data = {'username': request.data.get('username'),
                'nomeCompleto': request.data.get('nomeCompleto'),
                'email': request.data.get('email'),
                'password': request.data.get('password')}

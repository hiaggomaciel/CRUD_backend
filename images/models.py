from django.db import models


def upload_to(instance, filename):
    return f'images/{instance.user.id}/{filename}'

class User(models.Model):
    nomeCompleto = models.CharField(max_length=255, verbose_name="Nome Completo")
    username = models.CharField(max_length=50, verbose_name="Nome de Usuário")
    email = models.EmailField(max_length=50, verbose_name="Email")
    password = models.CharField(max_length=50, verbose_name="Senha")
    
    def __str__(self) -> str:
        return self.username

class ImageUpload(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Imagem")
    image = models.ImageField(upload_to=upload_to, verbose_name="Imagem")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuário")

    def __str__(self) -> str:
        return self.name

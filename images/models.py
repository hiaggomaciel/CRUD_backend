from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


def upload_to(instance, filename):
    return f'images/{instance.user.id}/{filename}'


class ImageUpload(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_to)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuário")

    def __str__(self) -> str:
        return self.name

from django.db import models

def upload_image_user(instance, filename):
    return f'{instance.id}-{filename}'

class Usuario(models.Model):
    user = models.CharField(max_length=30, unique=True, )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, unique=True)
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_image_user, blank=True, null=True)
    

    def __str__(self):
        return self.name


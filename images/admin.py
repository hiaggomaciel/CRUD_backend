from django.contrib import admin
from .models import ImageUpload, User

class Imagens(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'user')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(ImageUpload, Imagens)

class NewUser(admin.ModelAdmin):
    list_display = ('id', 'nomeCompleto', 'username', 'password', 'email')
    list_display_links = ('nomeCompleto',)
    search_fields = ('nomeCompleto',)
    
admin.site.register(User, NewUser)

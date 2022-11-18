from django.contrib import admin
from .models import Image, User

class Imagens(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'user_id')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Image, Imagens)

class NewUser(admin.ModelAdmin):
    list_display = ('id', 'nomeCompleto', 'username', 'password', 'email')
    list_display_links = ('nomeCompleto',)
    search_fields = ('nomeCompleto',)
    
admin.site.register(User, NewUser)

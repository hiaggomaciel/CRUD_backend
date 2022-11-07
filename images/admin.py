from django.contrib import admin
from .models import ImageUpload
from django.contrib.auth.models import User

class Imagens(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'user')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(ImageUpload, Imagens)

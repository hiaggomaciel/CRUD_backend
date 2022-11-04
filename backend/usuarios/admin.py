from django.contrib import admin
from usuarios.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email', 'password')
    list_display_links = ('id', 'name')
    #search_fields = ('name',)
    #list_filter = ('user',)
    list_per_page = 10
    #ordering = ('name',)
    
    
admin.site.register(Usuario, Usuarios)
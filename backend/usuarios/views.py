from rest_framework import viewsets
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    """Listando todos os usuários"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

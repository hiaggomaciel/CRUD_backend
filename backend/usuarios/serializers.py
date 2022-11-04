from rest_framework import serializers
from usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
    def validate_name(self, name):
        if not name.isalpha():
            raise serializers.ValidationError("Não inclua números neste campo")
        return name
    
    def validate_user(self, user):
        if user in Usuario:
            raise serializers.ValidationError("Usuário existente")
        return user
from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *


class ClienteSerializer(serializers.ModelSerializer):
    """Exibindo todos os clientes"""
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        # data = dados que estão vindo do request
        """Fazendo a validação do CPF"""
        if not cpf_valido(data['cpf']):
            # data["cpf"] = pegando o valor do campo cpf
            raise serializers.ValidationError({'cpf': 'O CPF deve ter 11 dígitos'})
            # {'campo': 'mensagem de erro'}
    
        """Fazendo a validação do nome"""
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome deve conter apenas letras'})
    
        """Fazendo a validação do RG"""
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve ter 9 dígitos'})
    
        """Fazendo a validação do celular"""
        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular':'O número de celular deve seguir o padrão: 00 00000-0000, respeitando o espaço e o hífen'})
        return data
